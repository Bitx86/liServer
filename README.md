# liServer
Another lightweight and modular Python-based web server (still under development). The idea of ​​this project is to be simple, so that it can be read and understood by anyone who is learning about HTTP requests, servers and similar things.

---
## Features

- **Modular Handler**: The server has a flexible request handler, allowing customization for different use cases.
- **Configurable Settings**: Settings like IP, port, and logging can be configured using a YAML file.
- **Logging**: Option to log incoming requests to a file for analysis and debugging.
- **Basic Request Handling**: The server can process incoming requests, though more advanced features (like HTML response handling) are planned.

---

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries (for now, `socketserver` and `PyYAML`)

## Known Issues
Well, actually, there's still a LOT of stuff missing (project just started), so I'll implement it when possible. However, there are a few things I plan to implement soon:

- Response handling is still in progress, with support for HTML responses planned in the future.

- Error handling is basic and might need improvements to make it less rudimentary.
  
## License
This project is open source and available under the MIT License. See the LICENSE file for more details.

## Contributing
Although I've barely started the project, contributions or ideas are welcome! Fork the repository and submit a pull request with your changes. Please make sure all code follows the existing style (not for “standard” purposes, but to be more user-friendly) and include tests if applicable.
