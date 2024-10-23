# Anthropic Quickstarts

### Computer Use Demo

An environment and tools that Claude can use to control a desktop computer. This project demonstrates how to leverage the computer use capabilities of the the new Claude 3.5 Sonnet model.

[Go to Computer Use Demo Quickstart](./computer-use-demo)

## Contributing

We welcome contributions to the Anthropic Quickstarts repository! If you have ideas for new quickstart projects or improvements to existing ones, please open an issue or submit a pull request.

## Community and Support

- Join our [Anthropic Discord community](https://www.anthropic.com/discord) for discussions and support
- Check out the [Anthropic support documentation](https://support.anthropic.com) for additional help

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

==========

<!-- notes in computer-use-demo/dockerfile -->
<!-- don't use dev-requirements.txt, wrong version, use requirements.txt in computer_use_demo/ -->

### Instructions for building the docker image:

`cd computer-use-demo`

Add your Browserbase API and Project ID to the `.env` file or in main() in browserbase.py:

`docker build -t my-computer-use-demo .`

Run the container with your Anthropic API key:
```bash
docker run \
    -e ANTHROPIC_API_KEY=<your-anthropic-api-key> \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5900:5900 \
    -p 8501:8501 \
    -p 6080:6080 \
    -p 8080:8080 \
    -it my-computer-use-demo
```
