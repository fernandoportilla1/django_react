

def country_image_upload_location(instance, filename):
    return 'media/country/images/%s%s.png' % (instance.id, filename)
