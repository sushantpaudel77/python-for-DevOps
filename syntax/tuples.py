# Tuple creation (immutable)
coordinates = (10.5, 20.3)
server_info = ("web1", "192.168.1.10", 80)

# Tuple unpacking
name, ip, port = server_info
print(f"Server: {name} at {ip}:{port}")

# Tuple methods
numbers = (1, 2, 3, 2, 4, 2)
print(numbers.count(2))      # Count occurrences: 3
print(numbers.index(3))      # Find index: 2

# Named tuples (more readable)
from collections import namedtuple
Server = namedtuple('Server', ['name', 'ip', 'port'])
web_server = Server('web1', '192.168.1.10', 80)
print(web_server.name)       # Access by name
print(web_server.ip)

# Tuple vs List choice
# Use tuple for: coordinates, database records, function returns
# Use list for: dynamic collections that change

# Tuple as dictionary key (hashable)
location = {(40.7128, -74.0060): "New York", (34.0522, -118.2437): "Los Angeles"}
print(location[(40.7128, -74.0060)])  # Output: New York

# Returning multiple values from a function
def get_user():
    return ("sushant", 25)

username, age = get_user()
print(f"User: {username}, Age: {age}")

# Employee data tuple (new example)
employee_data = ("John Doe", "Software Engineer", 75000, "Engineering", True)
emp_name, position, salary, department, is_active = employee_data
print(f"Employee: {emp_name}")
print(f"Position: {position} in {department}")
print(f"Salary: ${salary:,}")
print(f"Status: {'Active' if is_active else 'Inactive'}")

# Tuple representing a CI/CD pipeline step
pipeline_step = ("Build", {"tool": "Maven", "timeout": 300, "retries": 2})
step_name, step_config = pipeline_step
print(f"Step: {step_name}")
print(f"Tool: {step_config['tool']}, Timeout: {step_config['timeout']}s, Retries: {step_config['retries']}")

# Tuple representing an infrastructure monitoring alert
alert_info = ("CPU Usage High", "Critical", False)
alert_name, severity, is_resolved = alert_info
print(f"Alert: {alert_name}")
print(f"Severity: {severity}")
print(f"Resolved: {'Yes' if is_resolved else 'No'}")


# Tuple representing a Kubernetes Pod status
pod_status = ("frontend-pod-1", "Running", "2025-08-14T10:32:00Z")
pod_name, status, last_restart = pod_status
print(f"Pod: {pod_name} | Status: {status} | Last Restart: {last_restart}")

# Tuple for AWS EC2 instance details
ec2_instance = ("i-0abcd1234ef567890", "t3.medium", "us-east-1a", "running")
instance_id, instance_type, az, ec2_state = ec2_instance
print(f"EC2 ID: {instance_id}, Type: {instance_type}, AZ: {az}, State: {ec2_state}")

# Tuple for Docker image build info
docker_image = ("app-service", "v1.2.3", "dockerhub.com/org/app-service:v1.2.3")
image_name, version, repo_url = docker_image
print(f"Image: {image_name}:{version} ({repo_url})")

# Tuple for CI job result
ci_job = ("Unit Tests", "Passed", 132)  # 132 seconds
job_name, job_result, duration = ci_job
print(f"Job: {job_name} | Result: {job_result} | Duration: {duration}s")

# Tuple for Terraform resource creation
terraform_resource = ("aws_s3_bucket", "prod-logs", True)
resource_type, resource_name, creation_success = terraform_resource
print(f"Terraform: {resource_type} '{resource_name}' created: {creation_success}")

# Tuple for Git commit info
git_commit = ("a1b2c3d", "Fix memory leak in API handler", "Sushant", "2025-08-13")
commit_hash, commit_msg, author, date = git_commit
print(f"Commit {commit_hash} by {author} on {date}: {commit_msg}")

# Tuple for Jenkins pipeline stage
jenkins_stage = ("Deploy to Staging", {"parallel": False, "timeout": 600})
stage_name, stage_config = jenkins_stage
print(f"Stage: {stage_name} | Timeout: {stage_config['timeout']}s | Parallel: {stage_config['parallel']}")

# Tuple for Ansible playbook result
ansible_play = ("webservers.yml", "Completed", 12)  # 12 tasks executed
playbook, play_status, tasks_executed = ansible_play
print(f"Playbook: {playbook} | Status: {play_status} | Tasks: {tasks_executed}")

# Tuple for monitoring metric threshold
metric_alert = ("Memory Usage", 85, "Warning")  # 85% usage
metric_name, current_value, severity = metric_alert
print(f"Metric: {metric_name} | Current: {current_value}% | Severity: {severity}")

# Tuple for API endpoint uptime check
api_check = ("GET /health", True, 0.032)  # 32ms response
endpoint, is_healthy, response_time = api_check
print(f"Endpoint: {endpoint} | Healthy: {is_healthy} | Response: {response_time*1000:.1f}ms")

