from typing import TYPE_CHECKING, Any, Dict, Union
 
from ansiblelint.rules import AnsibleLintRule
 
if TYPE_CHECKING:
    from typing import Optional
 
    from ansiblelint.file_utils import Lintable
 

class TaskHasNameRule(AnsibleLintRule):
    id = "unnamed-task"
    shortdesc = "All tasks should be named"
    description = (
        "All tasks should have a distinct name for readability "
        "and for ``--start-at-task`` to work"
    )
    severity = "MEDIUM"
    tags = ["idiom"]
    version_added = "historic"
 
    def matchtask(
        self, task: Dict[str, Any], file: "Optional[Lintable]" = None
    ) -> Union[bool, str]:
        return not task.get("name")
