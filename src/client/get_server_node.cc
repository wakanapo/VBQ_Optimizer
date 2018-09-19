#include <algorithm>
#include <fstream>
#include <iostream>

#include "get_server_node.hpp"

std::vector<std::string> getNodes(std::string& filename) {
  std::vector<std::string> nodes;
  std::string line;
  std::ifstream ifs(filename);
  if (ifs.fail()) {
    std::cerr << "Error: Faild to read host file." << std::endl;
    exit(1);
  }
  while (getline(ifs, line)) {
    nodes.push_back(std::string(line.begin(),
                    std::find(line.begin(), line.end(), ' ')));
  }
  return nodes;
}

std::string findIP(std::string& filename, std::string nodename) {
  std::string line;
  std::ifstream ifs(filename);
  if (ifs.fail()) {
    std::cerr << "Error: Faild to read hosts file." << std::endl;
    exit(1);
  }
  while (getline(ifs, line)) {
    auto itr = std::search(line.begin(), line.end(),
                         nodename.begin(), nodename.end());
    if (itr == line.end())
      continue;
    if (*(itr + nodename.size()) == ' ' ||
        *(itr + nodename.size()) != '\n') {
      return std::string(line.begin(),
                         std::find(line.begin(), line.end(), ' '));
    }
    continue;
  }
  std::cerr << "Error: IP is not found." << std::endl;
  exit(1);
}

Server Server::setup() {
  std::string host_file = std::getenv("GA_HOSTFILE");
  std::string hosts = std::getenv("HOSTS");
  std::vector<std::string> nodes = getNodes(host_file);
  Server server;
  for (auto n : nodes) {
    server.ports_.push_back(findIP(hosts, n));
  }
  return server;
}

const std::vector<std::string>& Server::getPorts() {
  return ports_;
}

