# denite kind: ref
# Version: 0.1.1
# Author : JINNOUCHI Yasushi <me@delphinus.dev>
# License: MIT License
#          <https://opensource.org/licenses/mit-license.php>

from denite.kind.openable import Kind as Base
from denite.util import Candidate, Nvim, UserContext
from typing import Optional


class Kind(Base):
    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = "ref"

    # Needed for openable actions
    def action_open(self, context: UserContext) -> None:
        for target in context["targets"]:
            self.vim.call(
                "ref#open",
                target["action__ref_name"],
                target["word"],
                {"new": 1, "open": "edit"},
            )

    # Needed for openable actions
    def _winid(self, target: Candidate) -> Optional[int]:
        winid = self.vim.funcs.bufwinid(
            f"[ref-{target['action__ref_name']}:{target['word']}]"
        )
        return None if winid == -1 else winid
