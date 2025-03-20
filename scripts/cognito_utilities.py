import boto3
import argparse

parser = argparse.ArgumentParser(
    description="Add users to the Admin group in a Cognito User Pool."
)
parser.add_argument(
    "--user-pool-id",
    required=True,
    help="The ID of the Cognito User Pool to add users to.",
)
parser.add_argument(
    "--username",
    nargs="+",
    required=True,
    help="The username of the users to add to the Admin group.",
)
parser.add_argument(
    "--create-group",
    # required=True,
    action="store_true",
    help="Create the group",
)
parser.add_argument(
    "--group-name",
    required=True,
    default=None,
    help="The username of the users to add to the Admin group.",
)
parser.add_argument(
    "--region",
    required=False,
    default="us-east-1",
    help="The region of the Cognito User Pool.",
)
parser.add_argument(
    "--list-groups", action="store_true", help="List all groups in the User Pool."
)


# Initialize a Cognito Identity Provider client
client = boto3.client("cognito-idp", region_name="us-east-1")

user_pool_id = ARGS.user_pool_id
admin_group_name = ARGS.group_name


# Function to list all groups in a User Pool
def list_groups(pool_id):
    groups = []
    try:
        response = client.list_groups(UserPoolId=pool_id)
        groups = response["Groups"]
        while "NextToken" in response:
            response = client.list_groups(
                UserPoolId=pool_id, NextToken=response["NextToken"]
            )
            groups.extend(response["Groups"])
    except Exception as e:
        print(f"Error listing groups: {e}")
    return groups


# Function to list users in a specific group
def list_users_in_group(pool_id, group_name):
    users = []
    try:
        response = client.list_users_in_group(UserPoolId=pool_id, GroupName=group_name)
        users = response["Users"]
        while "NextToken" in response:
            response = client.list_users_in_group(
                UserPoolId=pool_id,
                GroupName=group_name,
                NextToken=response["NextToken"],
            )
            users.extend(response["Users"])
    except Exception as e:
        print(f"Error listing users in group {group_name}: {e}")
    return users


# Function to create a group if it doesn't exist
def create_group(pool_id, group_name):
    try:
        client.create_group(GroupName=group_name, UserPoolId=pool_id)
    except client.exceptions.GroupExistsException:
        print(f"Group '{group_name}' already exists.")


# Function to add a user to the group
def add_user_to_group(username, pool_id, group_name):
    response = client.admin_add_user_to_group(
        Username=username, UserPoolId=pool_id, GroupName=group_name
    )
    return response


def main(args):
    # Optionally create group first
    if args.create_group:
        create_group(user_pool_id, admin_group_name)

    # Add each user to the admin group
    for username in args.username:
        print(f"Adding {username} to {admin_group_name}...")
        add_user_to_group(username, user_pool_id, admin_group_name)
        print(f"Added {username} to {admin_group_name}")

    if args.list_groups:
        # Retrieve all groups
        groups = list_groups(user_pool_id)

        # Print each group and its users
        for group in groups:
            print(f"Group: {group['GroupName']} (Description: {group['Description']})")
            users = list_users_in_group(user_pool_id, group["GroupName"])
            print("Users:")
            for user in users:
                print(f"- {user['Username']} (Status: {user['UserStatus']})")
            print("\n" + "-" * 40 + "\n")


if __name__ == "main":
    args = parser.parse_args()
    main(args)
