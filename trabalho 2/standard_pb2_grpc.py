# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import standard_pb2 as standard__pb2


class StandardStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/standard.Standard/Create',
        request_serializer=standard__pb2.StandardRequest.SerializeToString,
        response_deserializer=standard__pb2.StandardReply.FromString,
        )
    self.Read = channel.unary_unary(
        '/standard.Standard/Read',
        request_serializer=standard__pb2.StandardRequest.SerializeToString,
        response_deserializer=standard__pb2.StandardReply.FromString,
        )
    self.Update = channel.unary_unary(
        '/standard.Standard/Update',
        request_serializer=standard__pb2.StandardRequest.SerializeToString,
        response_deserializer=standard__pb2.StandardReply.FromString,
        )
    self.Delete = channel.unary_unary(
        '/standard.Standard/Delete',
        request_serializer=standard__pb2.StandardRequest.SerializeToString,
        response_deserializer=standard__pb2.StandardReply.FromString,
        )
    self.Restart = channel.unary_unary(
        '/standard.Standard/Restart',
        request_serializer=standard__pb2.ResetRequest.SerializeToString,
        response_deserializer=standard__pb2.StandardReply.FromString,
        )


class StandardServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Read(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Restart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StandardServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=standard__pb2.StandardRequest.FromString,
          response_serializer=standard__pb2.StandardReply.SerializeToString,
      ),
      'Read': grpc.unary_unary_rpc_method_handler(
          servicer.Read,
          request_deserializer=standard__pb2.StandardRequest.FromString,
          response_serializer=standard__pb2.StandardReply.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=standard__pb2.StandardRequest.FromString,
          response_serializer=standard__pb2.StandardReply.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=standard__pb2.StandardRequest.FromString,
          response_serializer=standard__pb2.StandardReply.SerializeToString,
      ),
      'Restart': grpc.unary_unary_rpc_method_handler(
          servicer.Restart,
          request_deserializer=standard__pb2.ResetRequest.FromString,
          response_serializer=standard__pb2.StandardReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'standard.Standard', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))