from db_rsk_pred.database.DB import DB
from config import config_from_ini
from db_rsk_pred.predict import predict
from db_rsk_pred.database.write_to_db import write_db
import os
import argparse
from datetime import datetime
from db_rsk_pred.util.util import logger


def main():
    # global param
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cfg", default='./cfg_lung.ini')
    # global_args = parser.parse_args()

    # pred param
    parser.add_argument("-pd", "--test_data", default='None')
    parser.add_argument("-M", "--model", default='./model.json')
    parser.add_argument("-e", "--explain", default='True', choices=['True', 'False'])
    parser.add_argument("-db", "--to_db", default='True', choices=['True', 'False'])
    args = parser.parse_args([])  # [] 让解析器不要去解析CLI
    # fetch new data from DB
    cfg = config_from_ini(
        open(args.cfg, 'rt', encoding='utf-8'), read_from_file=True)
    db = DB(cfg.db.host, cfg.db.port, cfg.db.user, cfg.db.password, cfg.db.db,
            cfg.source.table, cfg.source.cols, cfg.source.tgt)
    sql = f'select {cfg.source.cols},{cfg.source.tgt} from {cfg.source.table} where etl_time>=date_sub(curdate(), interval 5 day) limit 100'  # 5天前
    print(sql)
    data = db.fetch_data_new(sql_str=sql)
    print(data.info())
    # judge empty dataframe(if have updating datas)
    if data.empty:
        message = "There's no new update datas, exit!"
    else:

        if eval(cfg.result.save):
            # save to csv like 20230515_113718.csv
            if not os.path.exists('./data'):
                os.mkdir('./data')
            now = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = f"./data/{now}.csv"
            data.to_csv(save_path, index=False)
            logger.info(f'{save_path.split("/")[-1]}  saved to csv')
            # predict
            args.test_data = save_path
            result_df = predict(args)

            # save to csv
            save_path = f'./data/{now}_result.csv'
            result_df.to_csv(save_path, index_label='idx')
            logger.info(f'{save_path.split("/")[-1]}  saved to csv')

        else:
            # predict
            result_df = predict(args, data=data)

        print(result_df.info())

        #  save to DB
        if eval(args.to_db):
            # save_path = path
            write_db(args.cfg, result_df=result_df)
        message = "successfull update!"

    print(message)
    return message


if __name__ == '__main__':
    message = main()