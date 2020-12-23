import json
import errno
import sys
import os
from s3_func import s3_push_delete_local

def _mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python ≥ 2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def _return_corners(aoi):

    with open(aoi) as f:
      geo_data = json.load(f)
    geo_data

    print(type (geo_data['features'][0]['geometry']))
    print(geo_data['features'][0]['geometry']['coordinates'][0])
    nw = geo_data['features'][0]['geometry']['coordinates'][0][3]
    print(nw)
    se = geo_data['features'][0]['geometry']['coordinates'][0][1]
    se
    return nw, se


aoi='project_aoi.geojson'

nw,se = _return_corners(aoi)

print(nw,se)

def _run_command(cmd, verbose=False):
    if verbose:
        print(cmd)
    result = os.system(cmd)
    if result != 0:
        raise Exception('command "%s" failed with code %d.' % (cmd, result))

def scrape_range_data(year):
    url='/vsicurl/http://rangeland.ntsg.umt.edu/data/rap/rap-vegetation-cover/v2'
    band = ' -b 1 '
    # window = f' {nw[0]} {nw[1]}, {se[0]} {se[1]} '
#     print(window)
    cmd='gdal_translate -co compress=lzw -co tiled=yes -co bigtiff=yes '
    
    _mkdir_p('TIF')

    out_bucket='dev-et-data'
    out_prefix='logan/in/raw/range_grass'
    filen = f'vegetation-cover-v2-{year}.tif'

#     full_cmd = cmd + band + ' -projwin ' + window + url + '/' + filen + ' TIF/' + filen
    full_cmd = cmd + band  + url + '/' + filen + ' TIF/' + filen
    print(full_cmd)

    _run_command(full_cmd, True)

    bucket = 'eco-w1'
    bucket_filepath = f'in0/rapv2/vegetation-cover-v2-{year}.tif'
    local_file = f'TIF/vegetation-cover-v2-{year}.tif'

    s3_push_delete_local(local_file,bucket,bucket_filepath)

    _run_command('aws s3 ls --human s3://eco-w1/in0/rapv2/')

    # _run_command(' rio info s3://dev-et-data/logan/in/raw/range_grass/vegetation-cover-v2-2019.tif | python -m json.tool')



if __name__ == "__main__":
    for int_year in range(1984, 2019+1):
    #for int_year in range(2009, 2017+1):
        year = str(int_year)
        scrape_range_data(year)

