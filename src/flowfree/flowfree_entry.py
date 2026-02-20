import os
import sys


package_root = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(package_root))
if project_root not in sys.path:
    sys.path.append(project_root)
if package_root not in sys.path:
    sys.path.append(package_root)
os.chdir(project_root)


try:
    import pygit2

    pygit2.option(pygit2.GIT_OPT_SET_OWNER_VALIDATION, 0)

    repo = pygit2.Repository(project_root)
    branch_name = repo.head.shorthand

    remote_name = 'origin'
    remote = repo.remotes[remote_name]
    remote.fetch()

    local_branch_ref = f'refs/heads/{branch_name}'
    local_branch = repo.lookup_reference(local_branch_ref)

    remote_reference = f'refs/remotes/{remote_name}/{branch_name}'
    remote_commit = repo.revparse_single(remote_reference)

    merge_result, _ = repo.merge_analysis(remote_commit.id)

    if merge_result & pygit2.GIT_MERGE_ANALYSIS_UP_TO_DATE:
        print("Already up-to-date")
    elif merge_result & pygit2.GIT_MERGE_ANALYSIS_FASTFORWARD:
        local_branch.set_target(remote_commit.id)
        repo.head.set_target(remote_commit.id)
        repo.checkout_tree(repo.get(remote_commit.id))
        repo.reset(local_branch.target, pygit2.GIT_RESET_HARD)
        print("Fast-forward merge")
    elif merge_result & pygit2.GIT_MERGE_ANALYSIS_NORMAL:
        print("Update failed - Did you modify any file?")
except Exception as e:
    print('Update failed.')
    print(str(e))

print('Update succeeded.')
from src.flowfree.launch import *
