# Tools

```bash
╰─$ pipenv run python cognito_admin_tools.py -h
usage: cognito_admin_tools.py [-h] --user-pool-id USER_POOL_ID --username USERNAME [USERNAME ...] [--create-group] --group-name GROUP_NAME
                              [--region REGION] [--list-groups]

Add users to the Admin group in a Cognito User Pool.

options:
  -h, --help            show this help message and exit
  --user-pool-id USER_POOL_ID
                        The ID of the Cognito User Pool to add users to.
  --username USERNAME [USERNAME ...]
                        The username of the users to add to the Admin group.
  --create-group        Create the group
  --group-name GROUP_NAME
                        The username of the users to add to the Admin group.
  --region REGION       The region of the Cognito User Pool.
  --list-groups         List all groups in the User Pool.
```
