import os
import argparse
import fsspec
import boto3

#######
IN_DIR='eco-w1/in0/rapv2'
OUT_DIR = 'eco-w1/in1/rapv2_cog/'
######-



def get_parser():
    parser = argparse.ArgumentParser(description='Run the code')
    parser.add_argument('-y', '--year', help='specify year or Annual or all example: -y 1999 ', default='Annual', type=str)
    return parser

def get_cog_src_dst(year):
    print(year)
    fs=fsspec.filesystem('s3', anon=False, requester_pays=True)
    non_cog_list = fs.ls(IN_DIR)
    for non_cog in non_cog_list:
        if year in non_cog:
            target_non_cog = non_cog

    file_obj = target_non_cog.split('/')[-1]
    dst_file_obj = OUT_DIR + file_obj


    return(f's3://{target_non_cog}',f's3://{dst_file_obj}')


def _run_command(cmd, verbose=False):
    if verbose:
        print(cmd)
    result = os.system(cmd)
    if result != 0:
        raise Exception('command "%s" failed with code %d.' % (cmd, result))

def _s3_push_delete_local(local_file, s3_full_object_path):
        s3 = boto3.client('s3')
        example = s3_full_object_path
        bucket = example.split('s3://')[-1].split('/')[0]
        prefix = '/'.join(example.split('s3://')[-1].split('/')[1:])
        print("s3 PUSH: ",local_file, s3_full_object_path)
        with open(local_file, "rb") as f:
            s3.upload_fileobj(f, bucket, prefix)
        os.remove(local_file)

def _cog_local_create_from_tif(src_tif,tmp_cog):
    command = f'rio cogeo create {src_tif} {tmp_cog}'
    print('CMD:: ', command)
    _run_command(command)

def cog_create_from_tif(src_tif,dst_cog):
    file_obj = dst_cog.split('/')[-1]
    local_tmp_cog = f'./{file_obj}'
    _cog_local_create_from_tif(src_tif,local_tmp_cog)
    _s3_push_delete_local(local_tmp_cog, dst_cog)


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    year = args['year']
    print(year)

    (src,dst) = get_cog_src_dst(year)
    print(src,dst)
    cog_create_from_tif(src,dst)

if __name__ == '__main__':
    command_line_runner()
