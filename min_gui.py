from dearpygui import dearpygui as dpg

# Create the context
dpg.create_context()

# Create a viewport (the application window)
dpg.create_viewport(title="Example Window", width=600, height=400)


# Define GUI elements within a window
with dpg.window(label="Main Window"):
    dpg.add_button(label="Click Me!")

# Setup and show the GUI
dpg.setup_dearpygui()
dpg.show_viewport()

# Start Dear PyGui's rendering loop
dpg.start_dearpygui()

# Cleanup
dpg.destroy_context()
