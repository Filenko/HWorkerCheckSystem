# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import run_pb2 as run__pb2


class RunnerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CheckProgram = channel.unary_unary(
                '/runner.Runner/CheckProgram',
                request_serializer=run__pb2.CodeWithTests.SerializeToString,
                response_deserializer=run__pb2.CheckResults.FromString,
                )


class RunnerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CheckProgram(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RunnerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CheckProgram': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckProgram,
                    request_deserializer=run__pb2.CodeWithTests.FromString,
                    response_serializer=run__pb2.CheckResults.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'runner.Runner', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Runner(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CheckProgram(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/runner.Runner/CheckProgram',
            run__pb2.CodeWithTests.SerializeToString,
            run__pb2.CheckResults.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
