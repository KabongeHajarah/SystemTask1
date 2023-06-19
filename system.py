class ExistingSystem:
    def __init__(self):
        # Initialize the existing system with default features
        self.feature1_enabled = True
        self.feature2_enabled = False

    def perform_feature1_action(self):
        if self.feature1_enabled:
            print("Performing Feature 1 action...")
        else:
            print("Feature 1 is not enabled.")

    def perform_feature2_action(self):
        if self.feature2_enabled:
            print("Performing Feature 2 action...")
        else:
            print("Feature 2 is not enabled.")

    def add_new_feature(self):
        # Implement the logic to add a new feature
        print("Adding a new feature...")
        # Update the necessary attributes and methods to support the new feature

    def update_feature(self, feature, enabled):
        # Update the status of a feature based on user input
        if feature == 1:
            self.feature1_enabled = enabled
            print("Feature 1 has been updated.")
        elif feature == 2:
            self.feature2_enabled = enabled
            print("Feature 2 has been updated.")
        else:
            print("Invalid feature number.")


# Example usage:
system = ExistingSystem()

# Perform existing features
system.perform_feature1_action()
system.perform_feature2_action()

# Add a new feature
system.add_new_feature()

# Update features based on user input
system.update_feature(1, True)  # Enable Feature 1
system.update_feature(2, True)  # Enable Feature 2

# Perform updated features
system.perform_feature1_action()
system.perform_feature2_action()
