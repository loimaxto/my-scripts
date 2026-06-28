import gitlab
import time

# 1. Setup connections
# No token needed for the public source, but you need your own token to create projects
MY_GITLAB_TOKEN = "YOUR_PERSONAL_ACCESS_TOKEN" 
PUBLIC_GROUP_ID = 987654321    # The ID of the public group you want to copy
MY_TARGET_GROUP_ID = 12345678  # The ID of your newly created empty group

gl_public = gitlab.GitLab('https://gitlab.com')
gl_mine = gitlab.GitLab('https://gitlab.com', private_token=MY_GITLAB_TOKEN)

# 2. Fetch all public projects from the target group
public_group = gl_public.groups.get(PUBLIC_GROUP_ID)
public_projects = public_group.projects.list(include_subgroups=True, all=True)

print(f"Found {len(public_projects)} public projects to copy.")

# 3. Import each project into your group via HTTP URL
for project in public_projects:
    print(f"Importing {project.name}...")
    
    try:
        gl_mine.projects.create({
            'name': project.name,
            'path': project.path,
            'namespace_id': MY_TARGET_GROUP_ID,
            'import_url': project.http_url_to_repo, # Imports via public HTTP address
            'visibility': 'private'                 # Can be 'private', 'internal', or 'public'
        })
        # Short sleep to avoid hitting API rate limits aggressively
        time.sleep(2)
    except Exception as e:
        print(f"Failed to import {project.name}. Error: {e}")

print("Process complete!")