import json
import multiprocessing
import checksumdir
from pathlib import Path
import time


class Checker:

    def __init__(self, concurrency=multiprocessing.cpu_count()):
        self.concurrency = concurrency
        self.queue = multiprocessing.Queue()

    def get_dirs_hash(self, full_path, index):
        self.queue.put(dict(index=index, file=str(full_path), checksum=checksumdir.dirhash(full_path)))

    def check_dir(self, directory):
        try:
            start = time.time()
            if Path(directory).is_dir():
                process_list = []
                index = 1
                for path in Path(directory).iterdir():
                    if path.is_dir():
                        p = multiprocessing.Process(target=self.get_dirs_hash, args=(path, index))
                        process_list.append(p)
                        index += 1
                if index == 1:
                    return {"message": "directory {} has no sub folders".format(directory)}

                for p in process_list:
                    p.start()

                return_dict = dict()
                return_dict["checksums"] = []
                for p in process_list:
                    returned_object = self.queue.get()
                    return_dict["checksums"].append(returned_object)
                    p.join()
                end = time.time()
                return_dict["metadata"] = dict(directory=directory,
                                               files=index-1,
                                               runtime=round(end-start, 2),
                                               concurrency=self.concurrency)

                return return_dict
            else:
                return {"message": "directory {} has no sub folders".format(directory)}
        except OSError as e:
            return {"message": "internal server error {}".format(e)}


if __name__ == '__main__':
    checker_instance = Checker()
    results = checker_instance.check_dir("/Users/orenspiegel/desktop/projects/tmp")
    print(json.dumps(dict(results), indent=2))







