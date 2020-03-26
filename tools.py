def parse_bg_image(data):
    return data.replace('url(//', '').replace(')', '')