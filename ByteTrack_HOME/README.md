### Prerequisite
Make sure CUDA and CUDNN are properly installed and related environment variables are properly set. 
Verified versions are anaconda3-5.1.0 + CUDA 10.0.130 + CUDNN 7.6.5 on Ubuntu 20.04.3 LTS. 

### Download the dataset
run the download_data.py file in the tools folder. The folders generated will be ignored by the .gitignore file, so the dataset wont be uploaded to github when saving this repository.

## Set Up ByteTrack
Follow ByteTrack instructions to [Installing on the host machine](https://github.com/ifzhang/ByteTrack#1-installing-on-the-host-machine). For the first step, the repo has already been cloned here.

### Run inference for each sequence
Let the path for the ByteTrack_HOME folder be <ByteTrack_HOME>
```
    export ByteTrack_HOME=<ByteTrack_HOME>
    cd <ByteTrack_HOME>
    export SN_TRACKING_MODE=test
    bash run_bytetrack_no_gt_batch.sh
```
To run challenge you should set the environment variable differently:
```
    export SN_TRACKING_MODE=challenge
```

### Zip and generate results for evaluation online
```
    cd <RESULT_FOLDER>
    zip soccernet_mot_results.zip SNMOT-???.txt
```
The generated soccernet_mot_results.zip can be submitted to the evaluation server.

### Evaluate locally

Generate gt.zip needed for evaluation
```
    python tools/zip_gt.py -f <SN_TRACKING_HOME>/test/

```

Run evaluation.

```
pip install git+https://github.com/JonathonLuiten/TrackEval.git

python tools/evaluate_soccernet_v3_tracking.py \
--TRACKERS_FOLDER_ZIP soccernet_mot_results.zip \
--GT_FOLDER_ZIP gt.zip \
--BENCHMARK SNMOT --DO_PREPROC False \
--SEQMAP_FILE tools/SNMOT-test.txt \
--TRACKERS_TO_EVAL test \
--SPLIT_TO_EVAL test \
--OUTPUT_SUB_FOLDER eval_results
```
It is expected to achieve a HOTA score of 71.5 on the test set.
