# Django Project Structure Configure

## Include Features
- Organized Apps directory
- Swagger Configuration for API Documentation
- Custom User Model and Authentication Endpoints with Unit Tests
- Environment Variable Configuration with Pydantic-Settings
- Predefined Logging Configuration
- Media/Static Files Configuration for Developement
- Pre-commit Linter Configuration
- Unit Test Configuration with Pytest
- Github Actions for Testing on Push


## Getting Started
After Downloading the Project Structure, In order to initialize the project correctly the following steps must be followed
- [ ] Create and Activate Virtual Environment for the Project
  - ```bash
    python3 -m venv venv && source venv/bin/Activate
    ```
- [ ] Install Required Packages
  - ```bash
    pip install -r requirements.txt
    ```

- [ ] Create an .env file in the project directly and copy the content of .env.example into it
- [ ] Install Pre-commit Hook to Run on Every Commit
  - ```bash
    pip install pre-commit && pre-commit install
    ```
