def generate_url(urls, apps=None, name=None):
    if apps is None:
        apps = []
    mapping = []

    mapping.extend(urls)

    for prefix, app_name in apps:
        if name == "__main__":
            app_path = app_name
        else:
            app_path = "%s.%s" % (name, app_name)
        app = __import__(app_path, fromlist=['mapping'])
        for app_url in app.mapping:
            new_url = list(app_url)

            new_url[0] = prefix + new_url[0]

            if isinstance(new_url[1], str):
                new_url[1] = "%s.%s" % (app_name, new_url[1])

            if len(app_url) == 4:
                new_url[3] = '%s.%s' % (app_name, new_url[3])
            mapping.append(tuple(new_url))
    return mapping
