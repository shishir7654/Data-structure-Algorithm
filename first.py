def qr_logo():

    def qr_code_generate():
        qr_logo()
        qr_size = raw_input("[+] Enter a size: ");
        qr_data = raw_input("[+] Specify a data for the QR Code : ");
        url = "https://chart.googleapis.com/chart?";
        size = "chs=" + qr_size;
        im1 = "&";
        qr = "cht=qr";
        im2 = "&";
        data = "chl=" + qr_data;
        im3 = "&";
        encode = "choe=UTF-8";
        generate = url + size + im1 + qr + im2 + data + im3 + encode;
        print( "[+]", generate);

    qr_code_generate()