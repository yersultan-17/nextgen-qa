# Anthropic Computer Use <> Browserbase Demo

<img src="anthropic-browserbase.png" alt="Anthropic Computer Use <> Browserbase Demo" width="500">

> [!CAUTION]
> Computer use is a beta feature. Please be aware that computer use poses unique risks that are distinct from standard API features or chat interfaces. These risks are heightened when using computer use to interact with the internet. To minimize risks, consider taking precautions such as:
>
> 1. Use a dedicated virtual machine or container with minimal privileges to prevent direct system attacks or accidents.
> 2. Avoid giving the model access to sensitive data, such as account login information, to prevent information theft.
> 3. Limit internet access to an allowlist of domains to reduce exposure to malicious content.
> 4. Ask a human to confirm decisions that may result in meaningful real-world consequences as well as any tasks requiring affirmative consent, such as accepting cookies, executing financial transactions, or agreeing to terms of service.
>
> In some circumstances, Claude will follow commands found in content even if it conflicts with the user's instructions. For example, instructions on webpages or contained in images may override user instructions or cause Claude to make mistakes. We suggest taking precautions to isolate Claude from sensitive data and actions to avoid risks related to prompt injection.
>
> Finally, please inform end users of relevant risks and obtain their consent prior to enabling computer use in your own products.

This repository helps you get started with computer use on Claude, with reference implementations of:

* Build files to create a Docker container with all necessary dependencies
* A computer use agent loop using the Anthropic API to access the updated Claude 3.5 Sonnet model
* Anthropic-defined computer use tools
* A streamlit app for interacting with the agent loop

> [!IMPORTANT]
> The Beta API used in this reference implementation is subject to change. Please refer to the [API release notes](https://docs.anthropic.com/en/release-notes/api) and [API reference](https://docs.browserbase.com/changelog) for the most up-to-date information.

> [!IMPORTANT]
> The components are weakly separated: the agent loop runs in the container being controlled by Claude, can only be used by one session at a time, and must be restarted or reset between sessions if necessary.

## Quickstart: running the Docker container

### Anthropic API

> [!TIP]
> You can find your API key in the [Anthropic Console](https://console.anthropic.com/).

### Browserbase API

> [!TIP]
> You can find your API key and project ID in the [Browserbase Settings](https://www.browserbase.com/settings).

### Instructions for building the docker image:

Go to the `computer-use-demo` directory:

```bash
cd computer-use-demo
```

Add your Browserbase API and Project ID to the `.env` file or in `main()` in `browserbase.py`:

```bash
docker build -t my-computer-use-demo .
```

Run the container with your Anthropic API key:

```bash
export ANTHROPIC_API_KEY=%your_api_key%
docker run \
    -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5900:5900 \
    -p 8501:8501 \
    -p 6080:6080 \
    -p 8080:8080 \
    -it my-computer-use-demo
```

### Accessing the demo app

Once the container is running, open your browser to [http://localhost:8080](http://localhost:8080) to access the combined interface that includes both the agent chat and desktop view.

The container stores settings like the API key and custom system prompt in `~/.anthropic/`. Mount this directory to persist these settings between container runs.

Alternative access points:

- Streamlit interface only: [http://localhost:8501](http://localhost:8501)
- Desktop view only: [http://localhost:6080/vnc.html](http://localhost:6080/vnc.html)
- Direct VNC connection: `vnc://localhost:5900` (for VNC clients)

## Screen size

Environment variables `WIDTH` and `HEIGHT` can be used to set the screen size. For example:

```bash
docker run \
    -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5900:5900 \
    -p 8501:8501 \
    -p 6080:6080 \
    -p 8080:8080 \
    -e WIDTH=1920 \
    -e HEIGHT=1080 \
    -it my-computer-use-demo
```

We do not recommend sending screenshots in resolutions above [XGA/WXGA](https://en.wikipedia.org/wiki/Display_resolution_standards#XGA) to avoid issues related to [image resizing](https://docs.anthropic.com/en/docs/build-with-claude/vision#evaluate-image-size).

Relying on the image resizing behavior in the API will result in lower model accuracy and slower performance than implementing scaling in your tools directly. The `computer` tool implementation in this project demonstrates how to scale both images and coordinates from higher resolutions to the suggested resolutions.

## Contributing

We welcome contributions to the Anthropic Computer Use <> Browserbase Demo repository! If you have ideas for new quickstart projects or improvements to existing ones, please open an issue or submit a pull request.

## Community and Support

- Email us [Browserbase Support](mailto:support@browserbase.com) for discussions and support
- Check out the [Browserbase documentation](https://docs.browserbase.com) for additional help

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.