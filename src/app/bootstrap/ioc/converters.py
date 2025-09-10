from typing import Protocol, TypeVar

Src_contra = TypeVar("Src_contra", contravariant=True)
Dst_co = TypeVar("Dst_co", covariant=True)


class ToOrmConverter(Protocol[Src_contra, Dst_co]):
    def __call__(self, src: Src_contra, /) -> Dst_co:
        raise NotImplementedError


class FromOrmConverter(Protocol[Src_contra, Dst_co]):
    def __call__(self, src: Src_contra, /) -> Dst_co:
        raise NotImplementedError
