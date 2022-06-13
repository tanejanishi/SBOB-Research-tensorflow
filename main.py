import tensorflow as tf

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hello = tf.constant("This is a Tensorflow Sbom PoC!")
    print_hi(hello)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
