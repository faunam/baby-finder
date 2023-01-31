from re import X
from fastai.vision.all import *
from urllib.request import urlretrieve
import os
import time


def classify(image_path, model=None):
    if not model:
        model = load_learner('babymodel.pkl')

    vocab = ['child', 'adult']
    prepped_img = PILImage.create(image_path)
    _,_,probs = model.predict(prepped_img)

    res = list(zip(vocab, [prob.item() for prob in probs]))
    
    return res

def download_image_from_url(url, destination):
    urlretrieve(url, destination)
    return destination

def filter_photos(photos_data):
    # receive photos object
    # create dictionary - id to metadata
    # 3 queues - download, process, delete
    # add all ids to download, pop and add to process, 
    # pop from process, classify,  add classification to dictionary
    # add to delete
    # pop from delete and delete.
    # any advantage to batching w/in these 3 steps
    # or does that only matter once we start multithreading
        # { media: [
    #       {
    #           baseUrl: ...,
#               filename: "PXL_20230119_232019676.jpg",
#               id: "AOrfjIOcznt5QAmrvgG1b5AB1Qn6bVdVDEe4FSREZBxQRxXpG6DhmOkjunl3a22YHopImgsZqyfF3AyW5GYZMnPGRY35m2tl3A"
#               mediaMetadata: {creationTime: '2023-01-19T23:20:19Z', width: '3024', height: '4032', photo: {…}}
#               mimeType: "image/jpeg",
#               productUrl: ...
#           },
    #  ...]}

    # lists of ids
    download = []
    process = []
    delete = []

    # hm i need a lookup table rather than a dictionary since there are other metadata fields here.
    # but for now im gonna do a bunch of dicts cuz its just faster to implement
   
    # key = id, value = baseUrl
    urls = {}
    # key = id, value = filename
    paths = {}
    # key = id, value = (classification, score)
    labels = {}

    # load model
    model = load_learner('babymodel.pkl')
    if not os.path.exists("imgs"):
        os.mkdir("imgs")

    for item in photos_data:
        urls[item["id"]] = item["baseUrl"]
        paths[item["id"]] = "imgs/" + item["filename"]
        download.append(item["id"])

    # for now this while loop / queuing seems kinda silly
    # but if i want to multithread its a good thing to set up i think.
    # i guess it wuold be better to implement it a simpler way if 
    # im not actually multithreading yet and then add in the 
    # queueing architecture, but whatver..
    while len(download) > 0:
        #download
        photo_id = download.pop(0)
        while paths[photo_id][-3:] == 'mp4':
            photo_id = download.pop(0)
        print("download", photo_id, time.time())
        filename = paths[photo_id]
        download_image_from_url(urls[photo_id], filename)
        process.append(photo_id) # only once image has downloaded. so .then or smth

        #process
        photo_id = process.pop(0)
        print("process", photo_id, time.time())
        res = classify(paths[photo_id], model)
        res_desc = sorted(res, key=(lambda label: label[1]), reverse=True)
        labels[photo_id] = res_desc[0]
        delete.append(photo_id) # only once image has processed. so .then or smth

        #delete
        photo_id = delete.pop(0)
        print("delete", photo_id, time.time())
        os.remove(paths[photo_id]) 
    
    return labels

ex = [
        {
            "baseUrl": "https://lh3.googleusercontent.com/lr/ANt_8_Ziu42yRuzur1jnIVXGrPmrWbL7N4R2W4RBTmBK-xUjRXOjZFOU534cKCdAJw0eCqOAT_MwBM2yLwb2k5Ik-zzBghlvqlX-F67XT7r_j2bp7TxSruklLhnGcuPMd49m7VDZ77b4AiT51cXSS1YDbYpihv5e3r8BMWrZ5hvYVOz65gwolNbAymhtm7eO9l08nWFGTY06xgPplJW42hDHiHVmm_oHOuMY6uBAU9u1nyedx1hKpU-1oGxjJk-aWlwmgR4K5QkO2O8CRIvMrDO6MFfUvz5iB1Ww0OKtl6d3aOfCGd0wxPGcmjWhw21Pr3egdUD14DNHWFXOszESzFIYZDuD8eZcJNiSgbdni9X8sccZTchScsOaFXgobQ473oK7me08tBQz-LwXLQyO1MNMrfy48obkCcjnefjh6LyZVUkr8E-Fyojgwyl_ZHEnp3_cF76F0W0hB8xjwSzDUYtYNkvhwnf5JoAA4C1TqjxukQ2QAbZVnGLNwPF3wP94ZxcEsckrSr7wi1vdxcKd5vp9snk4rZOcceSTTJzIc5vAEF12g661RUZeyJB3e6YEMZVQNfuC7rM2Tcarg4FbErBb_gqlUTgPrRME13WnuXg_WbqZgey04N0FkKaeSk0AGd-4fjA7nnqFxCUnjCMlTr7FICMm4afXH-q5HoV5YWs9CR02RgrXdTMkB6m95tskx7r-IGLqK9zcwDglpY7Ycl_FjVCmZrlF5e03NX96gdkBsZnqQ2dJJS1xhUR9sy5TqvR9DoazQ6ISujvINHVWveCBQAMSYJroXqFhrFwJGGiIgiukUnd86ICRw-KOaonOMy42NC0S4mhoRltecqSVli-v_cyG6gFzyyF2q9UF0t9kumm9JzO1CyxZTRCpRvGRHHefb8yHlRm7dAAkU8jrQ4_ltq0jceIbCaCIBMq0H9ArI0L_czwRdm5_yv6JpWA9_ui4X3_30QOUemreyRv12vpjYNewu11eu1D3gUeSkRdsPouD6-BxlnRJPoxjCNYit9E",
            "filename": "PXL_20230119_232019676.jpg",
            "id": "AOrfjIOcznt5QAmrvgG1b5AB1Qn6bVdVDEe4FSREZBxQRxXpG6DhmOkjunl3a22YHopImgsZqyfF3AyW5GYZMnPGRY35m2tl3A",
            "mediaMetadata": {"creationTime": '2023-01-19T23:20:19Z', "width": '3024', "height": '4032'},
            "mimeType": "image/jpeg",
          },
         {
            "baseUrl": "https://lh3.googleusercontent.com/lr/ANt_8_aV9FT2gPSZCKX-dX7_yNCwEZk_BpSo5-jyca8nu8tzGXOkvlunIpB-7u3yJO__38G2PraatVKirp_E8Tnp60hKyIQ5oUlPQu9wVDNzDFyoQqxzw1boICr-m5sgkT1U0dikXJmEflpUXTc6-d2SS5wggSeS9Dvg1M1dDro0IXGFjSfskEcTKsQUug7N-m2zsVT2iSkUH484h3gefJ12AEh4DkeYdhtiHXMZ4G55Po6ujMtZFf8ExbZMrMZIjtVm6PI7ZiS7greTKY6bJ9PEZMsifcucD_UzD6EGgmf0HgVSv6AZsW4Xy0jnb3xK-VnZVsIh6ZDeyiP192b4Ne7F-GrEx6rrtj1B2ga0QzdelN-2nov2cnf8jX_w5-i4L_mIM5qxEcqw-98O3XS4GoakkX7mw5muZiV0ADSfzucFwk8iGr1SzcNJkyNlsfQdsrqB4mqet__OkiDzOUT8hIa-eSG5PGe1eJZCDjuzlyfJW3fekTQC4S76tt6fa-AYKaciKxcNUBxOVKFdTYrwgU1f-fslbDYw-a4M1aSlmeDkRW6IDjRqcaozJVDZcF52QLsp6qGDakOG1PDES6O4tPJ7pBRHR-04yowSQOFFpqDxa4lR476bjrMPnsSPmM5GL0_FmjfqPvsvlnLJ60r23_NI7WB5Af3QgVBx62Qy0N26WOwepA2ynOZLzJr1qlzlxPOFsWzVoG5iVm0ztQeDBfAYnU7oaQoj2f0sjPWpezGj2NtQA4IqwSIYXtQ47aJzE_wjhSnwNquDIqzC9ufX4J21si0scm9YBME8X9ms0oJm35KTsnL_ywTQJeyuSS0JXIIn9YbMzdBgMKoposXofcVDl-iDh9nyw9ggxSQ_Z7rbN4yMe01CPNi9CPM0pfrp57uTSiYevy9RZRHV8eHTaJqhWSV7MgIMnfPN_l9Y65-v9-4x2TmXjgfTMbTiFZmRzOGSLsoPFjjRQx_92eoVAiYYdNrCATa2lb0ltRD6w2ehPxWO02-b0zJdh6zHHynUr2o",
            "filename": "PXL_20230126_011118372.jpg",
            "id": "AOrfjINhMA-TaXbcOW8WNk9y6vX5eVKlzafy8sxdP3fseJE6skJJfF9Q7z-ZhmZUkXKF5HnXcDgQBazc9NNKzWiTNjfQdEE82Q",
            "mediaMetadata": {"creationTime": '2023-01-19T23:20:19Z', "width": '3024', "height": '4032'},
            "mimeType": "image/jpeg",
          },
        {
            "baseUrl": "https://www.healthychildren.org/SiteCollectionImagesArticleImages/young-girl-in-a-hospital-bed-with-her-teddy-bear.jpg",
            "filename": "PXL_20230126_004048958.jpg",
            "id": "AOrfjIOEFXRz7TewM3ca4yT2W_PjzZyRg-aApwJb7Twqrov3olO6fHz3Hmeftt21kH2JnCUwOPznnra0g9Meip7-Aq6G9vxXcA",
            "mediaMetadata": {"creationTime": '2023-01-19T23:20:19Z', "width": '3024', "height": '4032'},
            "mimeType": "image/jpeg",
          }
    ]

def test100():
    start = time.time()

    ex100 = []
    with open('ex.json', 'r') as infile:
        ex100 = json.loads(infile.read())['mediaItems']

    end = time.time()
    print('load json', end - start)

    start = time.time()
    res =filter_photos(ex100)
    end = time.time()
    print(res)
    print('process 100', end - start)

# supposedly takes 16 seconds to process 100 photos, single thread.
# test100()