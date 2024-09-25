import plugins
from runner import ExtendableWebApp


def main():
    app = ExtendableWebApp()
    app.add_plugins(plugins)
    app.run()


if __name__ == "__main__":
    main()
