#include <string>
#include <vector>

class Nodes {
 public:
  static Nodes setup();
  const std::vector<std::string>& getAddresses();
 private:
  Nodes();
  std::vector<std::string> ports_;
};
