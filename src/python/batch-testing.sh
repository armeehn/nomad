#/bin/zsh

echo 'Starting batch testing...'
echo ''

for PROB_NUM in {19..21}
do
    for NUM_EVALS in {2,3}00 #{1,2,3}00 #{10..10}
    do
        echo "Doing Problem ${PROB_NUM}...${NUM_EVALS} BB EVALS."

        DATA_PATH="data/raw/problem-${PROB_NUM}/${NUM_EVALS}evals.txt"

        # and get the nomad data, but we have to create
        # some temporary stuff first because its the quickest
        # despite it being not the nicest
        PARAM_FILE="param-${PROB_NUM}.txt"
        # needs to be saved otherwise we'll lose it next invoke

        for i in {1..30}
        do

            SEED=$RANDOM
            SEED_PARAM_FILE="seed(${SEED})-${PARAM_FILE}"

            # append the seed paran
            cp $PARAM_FILE $SEED_PARAM_FILE
            echo "SEED  ${SEED}" >> $SEED_PARAM_FILE
            echo "MAX_BB_EVAL ${NUM_EVALS}" >> $SEED_PARAM_FILE

            nomad $SEED_PARAM_FILE  | grep "best feasible"  \
                                    | tr -s ' '             \
                                    | cut -d ' ' -f5-       \
                                    | tee -a $DATA_PATH

            # can redirect output with > to raw-data.txt
            # clean up using regex "\(.*\) h=0 "

            rm $SEED_PARAM_FILE

        done
        echo "-------------"
    done
done

echo "Batching testing complete."
