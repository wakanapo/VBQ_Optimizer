#include <iostream>
#include <memory>

#include <grpcpp/completion_queue.h>
#include <grpc/support/log.h>

#include "evaluate_server.hpp"
#include "util/color.hpp"

bool GenomEvaluationClient::
GetIndividualWithEvaluation(const GenomEvaluation::Genom& genom,
                            GenomEvaluation::Individual* individual) {
  grpc::ClientContext context;
  grpc::CompletionQueue cq;
  grpc::Status status;  
  std::unique_ptr<grpc::ClientAsyncResponseReader<GenomEvaluation::Individual>>
    rpc(stub_->AsyncGetIndividual(&context, genom, &cq));
  rpc->StartCall();
  rpc->Finish(individual, &status, (void*)1);
  void* got_tag;
  bool ok = false;
  GPR_ASSERT(cq.Next(&got_tag, &ok));
  GPR_ASSERT(got_tag == (void*)1);
  GPR_ASSERT(ok);
  
  if (!status.ok()) {
    std::cerr << coloringText("ERROR:", RED)
              << "GetIndividual rpc faild." << std::endl;
    return false;
  }
  if (!individual->has_genom()) {
    std::cerr << coloringText("ERROR:", RED)
              << "Server returns incomplete individual." << std::endl;
    return false;
  }
  return true;
}
