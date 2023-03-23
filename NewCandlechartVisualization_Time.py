import os
import glob
import pandas as pd
import plotly.graph_objs as go

image_num_check = 0
stock_num_check = 0
csv_list = ['OHLCV_data', 'OHLCV_data_10T', 'OHLCV_data_30T', 'OHLCV_data_H']

for csv in csv_list:
    csv_path = f"C:/Users/user/PycharmProjects/DaishinAPI/code_snippet/{csv}"
    csv_data = glob.glob(os.path.join(csv_path, "*.csv"))

    # 1. 데이터 폴더 및 라벨링 폴더 만들어주기
    if not os.path.exists(f'images_filtering_{csv[11:]}'):
        os.makedirs(f'./images_filtering_{csv[11:]}')
        os.makedirs(f'./images_filtering_{csv[11:]}/up_up')
        os.makedirs(f'./images_filtering_{csv[11:]}/up_down')
        os.makedirs(f'./images_filtering_{csv[11:]}/down_up')
        os.makedirs(f'./images_filtering_{csv[11:]}/down_down')
        os.makedirs(f'./images_filtering_{csv[11:]}/sideways')

    for i in csv_data:
        csv_name = os.path.basename(i)[:7]
        print(i)
        print('종목명: ' + csv_name)

        # 2. OHLCV 데이터 불러오기
        df = pd.read_csv(i, index_col=0, parse_dates=True, sep=',', names=['date', 'open', 'high', 'low', 'close', 'volume'])

        # 3. 날짜 변경 line 저장
        date_change_line_list = []
        check_day = None
        for i in range(len(df.index)) :
            # i 번째줄 date -> 날짜[4:8] : mmdd
            cur_day = df.index[i][5:10]

            # 날짜가 바뀐지 확인 후 리스트 추가 및 기준점 변경
            if check_day != cur_day :
                date_change_line_list.append(i)
                check_day = cur_day
        date_change_line_list = date_change_line_list[1:]

        # 4. 이미지 생성
        for i in range(len(date_change_line_list) - 1):
            start, end = date_change_line_list[i], date_change_line_list[i + 1] - 1
            # print(start, end)

            df_day = df[start:end]  # OHLCV 데이터 하루 단위 분할
            close_day = int(df_day['close'][-1:]) # 당일 종가
            open_day = int(df_day['open'][:1]) # 당일 시가
            close_one_tick = int(df_day['close'][-2:-1]) # 당일 마지막 직전 캔들 종가
            print('당일 종가: ' + str(close_day) + ' / ', '당일 시가: ' + str(open_day) + ' / ', '당일 마지막 직전 캔들 종가: ' + str(close_one_tick))

            # OHLCV 각각 별 리스트 생성
            open_list = df_day['open']
            high_list = df_day['high']
            low_list = df_day['low']
            close_list = df_day['close']
            volume_list = df_day['volume']

            # 이미지 생성 전 필터링 조건문 적용
            if abs(open_day - close_day) >= (int(max(high_list)) - int(min(low_list)))/2:

                fig = go.Figure(data=[go.Candlestick(x=df.index[start:end],
                                                     open=df['open'][start:end],
                                                     high=df['high'][start:end],
                                                     low=df['low'][start:end],
                                                     close=df['close'][start:end],
                                                     decreasing=dict(fillcolor='blue', line=dict(color='blue')), # 음봉: 파란색 설정
                                                     increasing=dict(fillcolor='red', line=dict(color='red')) # 양봉: 빨간색 설정
                                                     )])

                fig.update_layout(xaxis_rangeslider_visible=False, xaxis={'visible': False}, yaxis={'visible': False}) # x축, y축 등 기타 요소 안보이게 설정

                # 5. 이미지 라벨링 및 저장
                if close_day - open_day > 0:
                    if close_day - close_one_tick >= 0:
                        fig.write_image(f'images_filtering_{csv[11:]}/up_up/{csv_name}_{i}{0:05d}.png')  # up_up 폴더에 저장
                    elif close_day - close_one_tick < 0:
                        fig.write_image(f'images_filtering_{csv[11:]}/up_down/{csv_name}_{i}{0:05d}.png') # up_down 폴더에 저장
                elif close_day - open_day < 0:
                    if close_day - close_one_tick > 0:
                        fig.write_image(f'images_filtering_{csv[11:]}/down_up/{csv_name}_{i}{0:05d}.png')  # down_up 폴더에 저장
                    elif close_day - close_one_tick <= 0:
                        fig.write_image(f'images_filtering_{csv[11:]}/down_down/{csv_name}_{i}{0:05d}.png') # down_down 폴더에 저장
                else:
                    fig.write_image(f'images_filtering_{csv[11:]}/sideways/{csv_name}_{i}{0:05d}.png') # sideways 폴더에 저장

                image_num_check += 1
                print(f'이미지 {image_num_check}번째 생성')

            else:
                continue

        stock_num_check += 1

        print(f"------------------------------------------------------------------{csv_name} 종목({stock_num_check}번째) 끝------------------------------------------------------------------")