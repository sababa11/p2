import boto3
import p1


def print_dependencies():
    print("Importing boto3 version:%s" % boto3.__version__)
    print("Importing src1 version:%s" % p1.__version__)
    return True
