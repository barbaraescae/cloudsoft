# CloudSoft

CloudSoft is a Python program designed to create and manage user profiles with customizable settings for shared Windows computers. This tool allows different users to maintain personalized settings in a shared environment, enhancing the user experience.

## Features

- **Create User Profiles:** Easily create a new user profile with default settings.
- **Customizable Settings:** Update individual settings such as theme, wallpaper, notifications, and auto-updates.
- **Persistent Storage:** User profiles are saved to a JSON file, ensuring data is retained across sessions.

## Getting Started

### Prerequisites

- Python 3.x
- No additional libraries are required.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cloudsoft.git
    ```

2. Navigate to the project directory:
    ```bash
    cd cloudsoft
    ```

3. Run the program:
    ```bash
    python cloudsoft.py
    ```

## Usage

- **Creating a User Profile:**
  ```python
  cloud_soft.create_user_profile("john_doe")
  ```

- **Updating a User Setting:**
  ```python
  cloud_soft.update_user_setting("john_doe", "theme", "dark")
  ```

- **Retrieving User Settings:**
  ```python
  settings = cloud_soft.get_user_settings("john_doe")
  print(settings)
  ```

## Contributing

Contributions to CloudSoft are welcome! If you have suggestions or improvements, feel free to fork the repository and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the open-source community for continuous inspiration.