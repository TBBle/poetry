from __future__ import annotations

from typing import TYPE_CHECKING

from poetry.repositories import Repository


if TYPE_CHECKING:
    from poetry.core.packages.dependency import Dependency
    from poetry.core.packages.package import Package


class ResolvedRepository(Repository):
    """
    Special repository for holding and returning the already-resolved packages
    to be installed.
    It does not attempt to exclude pre-release packages.
    """

    def find_packages(self, dependency: Dependency) -> list[Package]:
        packages = []
        constraint, _allow_prereleases = self._get_constraints_from_dependency(
            dependency
        )
        for package in self.packages:
            if dependency.name == package.name and constraint.allows(package.version):
                packages.append(package)

        print(packages)
        return packages
