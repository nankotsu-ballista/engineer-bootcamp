import typing

# =========================================
# ceil_pow2: 2^k >= n を満たす最小の k を返す
# （atcoder._bit._ceil_pow2 の自前実装）
# =========================================
def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1
    return x


# =========================================
# 汎用 Lazy Segment Tree 本体
# （atcoder.lazy_segtree を Python で再現）
# =========================================
class LazySegTree:
    def __init__(
        self,
        op: typing.Callable[[typing.Any, typing.Any], typing.Any],
        e: typing.Any,
        mapping: typing.Callable[[typing.Any, typing.Any], typing.Any],
        composition: typing.Callable[[typing.Any, typing.Any], typing.Any],
        id_: typing.Any,
        v: typing.Union[int, typing.List[typing.Any]],
    ) -> None:
        """
        op:      区間をマージする演算（モノイドの二項演算）
        e:       op の単位元
        mapping: 遅延値 f をセグ木の値 x に適用する関数 mapping(f, x)
        composition: 遅延値同士の合成 composition(f, g) = f ◦ g
        id_:     遅延値の単位元（「何もしない」演算）
        v:       初期配列 or 長さ（int の場合はすべて e で初期化）
        """
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        self._lz = [self._id] * self._size

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    # ----- 単点 set / get -----
    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    # ----- 区間 prod -----
    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        if left == right:
            return self._e

        left += self._size
        right += self._size

        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push((right - 1) >> i)

        sml = self._e
        smr = self._e
        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    # ----- apply: 区間/一点に遅延演算をかける -----
    def apply(
        self,
        left: int,
        right: typing.Optional[int] = None,
        f: typing.Optional[typing.Any] = None,
    ) -> None:
        assert f is not None

        # 一点適用
        if right is None:
            p = left
            assert 0 <= p < self._n

            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = self._mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        # 区間適用
        else:
            left0 = left
            right0 = right
            assert 0 <= left <= right <= self._n
            if left == right:
                return

            left += self._size
            right += self._size

            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            l2 = left
            r2 = right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2

            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    # ----- max_right / min_left（必要なら使う） -----
    def max_right(
        self, left: int, g: typing.Callable[[typing.Any], bool]
    ) -> int:
        assert 0 <= left <= self._n
        assert g(self._e)

        if left == self._n:
            return self._n

        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not g(self._op(sm, self._d[left])):
                while left < self._size:
                    self._push(left)
                    left *= 2
                    if g(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(
        self, right: int, g: typing.Callable[[typing.Any], bool]
    ) -> int:
        assert 0 <= right <= self._n
        assert g(self._e)

        if right == 0:
            return 0

        right += self._size
        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(self._op(self._d[right], sm)):
                while right < self._size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    # ----- 内部ユーティリティ -----
    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k: int, f: typing.Any) -> None:
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k: int) -> None:
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = self._id


# =========================================
# 具体例: 区間加算 + 区間和
# （配列 a に対して、add / sum クエリ）
# =========================================

# 値は (sum, length) のタプルとして持つ
#   sum: その区間の総和
#   length: その区間の長さ
# def build_range_add_range_sum(a: typing.List[int]) -> LazySegTree:
#     # 区間マージ
#     def op(x, y):
#         return (x[0] + y[0], x[1] + y[1])

#     # 単位元
#     e = (0, 0)

#     # 遅延値 f を区間データ x に適用
#     # f: 加算する値
#     # x: (sum, length)
#     def mapping(f, x):
#         return (x[0] + f * x[1], x[1])

#     # 遅延値同士の合成
#     # 先に g、その上から f をかける → f + g（加算なので可換）
#     def composition(f, g):
#         return f + g

#     # 遅延値の単位元（何もしない）
#     id_ = 0

#     v = [(val, 1) for val in a]
#     return LazySegTree(op, e, mapping, composition, id_, v)

w,n=map(int,input().split())
lst=[0]*w
# 区間演算op
def op(data1, data2):
    return max(data1, data2)


# opの単位元 op(data1, e) = data1
e = -1


# lazyをdataに作用させる
def mapping(lazy_upper, data_lower):
    if lazy_upper == -1:
        return data_lower
    else:
        return lazy_upper


# lazyをlazyに作用させる
def composition(lazy_upper, lazy_lower):
    if lazy_upper == -1:
        return lazy_lower
    else:
        return lazy_upper


# mapping(_id, data_lower) = data_lower
_id = -1

lazy_segtree = LazySegTree(op, e, mapping, composition,_id,lst)

for _ in range(n):
    l, r = map(int, input().split())
    l -= 1
    max_height = lazy_segtree.prod(l, r)
    lazy_segtree.apply(l, r, max_height + 1)
    print(max_height + 1)
    

