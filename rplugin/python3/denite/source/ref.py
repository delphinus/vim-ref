# denite source: ref
# Version: 0.1.1
# Author : JINNOUCHI Yasushi <me@delphinus.dev>
# License: MIT License
#          <https://opensource.org/licenses/mit-license.php>

from denite.base.source import Base
from denite.util import Nvim, Candidates, UserContext


class Source(Base):
    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = "ref"
        self.kind = "ref"
        self.is_volatile = True

    def gather_candidates(self, context: UserContext) -> Candidates:
        if len(context["args"]) > 0:
            ref_name = context["args"][0]
        else:
            self.error_message(context, "Usage: Denite ref:<ref-source-name>")
            return []

        is_available = bool(
            self.vim.eval(f"has_key(ref#available_sources(), '{ref_name}')")
        )
        if not is_available:
            self.error_message(context, f"{ref_name} is not available")
            return []

        inp = context["input"]
        return [
            {"word": x, "action__ref_name": ref_name}
            for x in self.vim.eval(
                f"ref#available_sources()['{ref_name}'].complete('{inp}')"
            )
        ]
