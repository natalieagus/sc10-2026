## Working Repository for SC10 10.020 DDW

This repository will be updated weekly at the end of each lesson. Clone and pull for updates regularly.

We use `pre-commit` hook and `nbstripout`.

```
pip install pre-commit nbstripout
# run once recursively
find . -name "*.ipynb" -not -path "*/.ipynb_checkpoints/*" -exec nbstripout {} +
```

The pre-commit hook is used to block large files from being committed and run `nbstripout` automatically before each commit. Edit the `.yaml` file accordingly to adjust the size.

The hook has been installed and run once for the files:

```
pre-commit install
pre-commit run --all-files
```

You can see them under `.git/hooks`.

We also used `nbdime` to see `git diff` better with the notebooks.

```
pip install nbdime
nbdime config-git --enable
```
