from django.shortcuts import render
from django.shortcuts import render


def home(request):
    return render(request, 'portfolio/home.html')


def contact(request):
    return render(request, 'portfolio/contact.html')


def home(request):

    skills = [
        # Programming Languages
        {"name": "Java", "icon": "fab fa-java", "tip": "Object-oriented programming language"},
        {"name": "C#", "icon": "fas fa-code", "tip": "Microsoft .NET programming language"},

        # Operating Systems & System Administration
        {"name": "Linux Basics", "icon": "fab fa-linux", "tip": "Linux system administration and CLI"},
        {"name": "Windows Server Basics", "icon": "fas fa-server", "tip": "Basic administration of Windows Server"},

        # Scripting & Automation
        {"name": "Bash Basics", "icon": "fas fa-terminal", "tip": "Shell scripting and automation basics"},

        # CI/CD & DevOps Tools
        {"name": "GitHub Actions", "icon": "fab fa-github", "tip": "CI/CD automation with GitHub Actions"},
        {"name": "Version Control (Git)", "icon": "fab fa-git-alt", "tip": "Source control and team collaboration"},

        # Containerization & Orchestration
        {"name": "Docker", "icon": "fab fa-docker", "tip": "Containerization of applications with Docker"},

        # Infrastructure as Code / Config Management
        {"name": "IaC & Config Management", "icon": "fas fa-code-branch", "tip": "Infrastructure automation tools (e.g., Terraform, Ansible)"},

        # Cloud Platforms & Core Services
        {"name": "Microsoft Azure", "icon": "fas fa-cloud", "tip": "Azure Fundamentals and Core Services"},
        {"name": "AWS", "icon": "fab fa-aws", "tip": "Amazon Web Services (EC2, S3, IAM, etc.)"},
  
        # Cloud Security & Monitoring
        {"name": "Cloud Security", "icon": "fas fa-shield-alt", "tip": "Identity, access control, and threat protection"},
        {"name": "Monitoring", "icon": "fas fa-chart-line", "tip": "Logging and performance monitoring of systems"},

        # Networking & Security
        {"name": "Networking Basics", "icon": "fas fa-network-wired", "tip": "Subnetting, firewalls, and routing"},
        {"name": "Cloud Networking", "icon": "fas fa-project-diagram", "tip": "VPCs, subnets, and peering in cloud environments"},
        {"name": "System Security", "icon": "fas fa-lock", "tip": "Authentication, updates, and access control"},

        # Professional & Transferable Skills
        {"name": "Problem Solving", "icon": "fas fa-lightbulb", "tip": "Logical thinking and debugging"},
        {"name": "Time Management", "icon": "fas fa-clock", "tip": "Efficient task prioritization and planning"},
        {"name": "Communication", "icon": "fas fa-comments", "tip": "Clear and effective verbal/written communication"},
        {"name": "Teamwork", "icon": "fas fa-people-group", "tip": "Collaboration and interpersonal effectiveness"},
        {"name": "Planning & Organizing", "icon": "fas fa-calendar-check", "tip": "Project planning and scheduling"},
        {"name": "Adaptability", "icon": "fas fa-arrows-rotate", "tip": "Quick learning and flexibility"},
        {"name": "Leadership", "icon": "fas fa-user-tie", "tip": "Leading by example and motivating peers"},
    ]


    return render(request, 'portfolio/home.html', {"skills": skills})











