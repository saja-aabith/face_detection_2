import pkg_resources
import subprocess
import sys

# List of required packages and their versions
required_packages = {
    "face_recognition": "1.3.0",  # Replace with the required version
    "dlib": "19.22.0",            # Replace with the required version
    "numpy": "1.21.0"             # Replace with the required version
}

# Function to install a package
def install_package(package, version):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"{package}=={version}"])
        print(f"Successfully installed {package}=={version}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package}. Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while installing {package}: {e}")

# Ensure cmake is installed and available
try:
    import cmake
    print(f"cmake module is available: {cmake.__version__}")
except ModuleNotFoundError:
    print("cmake module is not available. Installing cmake...")
    install_package("cmake", "3.22.0")  # Replace with the required version

# Check installed packages and their versions
for package, required_version in required_packages.items():
    try:
        installed_version = pkg_resources.get_distribution(package).version
        if installed_version == required_version:
            print(f"{package} is installed with the correct version ({installed_version}).")
        else:
            print(f"{package} is installed with version {installed_version}, but version {required_version} is required.")
            print(f"Installing the correct version of {package}...")
            install_package(package, required_version)
    except pkg_resources.DistributionNotFound:
        print(f"{package} is not installed.")
        print(f"Installing {package}...")
        install_package(package, required_version)
    except Exception as e:
        print(f"An unexpected error occurred while checking {package}: {e}")