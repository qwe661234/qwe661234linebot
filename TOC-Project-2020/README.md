# TOC Project 2020

[![Maintainability](https://api.codeclimate.com/v1/badges/dc7fa47fcd809b99d087/maintainability)](https://codeclimate.com/github/NCKU-CCS/TOC-Project-2020/maintainability)

[![Known Vulnerabilities](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020/badge.svg)](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020)


Template Code for TOC Project 2020

A Line bot based on a finite state machine

More details in the [Slides](https://hackmd.io/@TTW/ToC-2019-Project#) and [FAQ](https://hackmd.io/s/B1Xw7E8kN)

## Setup

### Prerequisite
* Python 3.6
* Pipenv
* Facebook Page and App
* HTTPS Server

#### Install Dependency
```sh
pip3 install pipenv

pipenv --three

pipenv install

pipenv shell
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)
	* [Note: macOS Install error](https://github.com/pygraphviz/pygraphviz/issues/100)


#### Secret Data
You should generate a `.env` file to set Environment Variables refer to our `.env.sample`.
`LINE_CHANNEL_SECRET` and `LINE_CHANNEL_ACCESS_TOKEN` **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

#### a. Ngrok installation
* [ macOS, Windows, Linux](https://ngrok.com/download)

or you can use Homebrew (MAC)
```sh
brew cask install ngrok
```

**`ngrok` would be used in the following instruction**

```sh
ngrok http 8000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```

#### b. Servo

Or You can use [servo](http://serveo.net/) to expose local servers to the internet.


## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* state:user

	* Input: "吃吃"
	  * state: eat
	  * title: "吃吃 choose"
	  * Reply: 三個按鈕:
	  	1. 北部 
	  	2. 中部 
	 	3. 南部

		* Input: 選擇按鈕 "北部"
		  * state: north
		  * Reply: 兩個圖文選單  
		  	* 選單1 
				   title: "在台北吃吃 選個"\
				   	兩個按鈕: 
					1. PTT美食
					2. 別的地方好了
			* 選單2
				   title: "在桃園吃吃 選個"\
				   	兩個按鈕: 
					1. PTT美食
					2. 別的地方好了
		

		* Input: 選擇按鈕 "中部"
		  * state: middle
		  * Reply: 兩個圖文選單  
		  	* 選單1 
				   title: "在台中吃吃 選個"\
				   	兩個按鈕: 
					1. PTT美食
					2. 別的地方好了
			* 選單2
				title: "在彰化吃吃 選個"\
				兩個按鈕: 
				1. PTT美食
				2. 別的地方好了

		* Input: 選擇按鈕 "南部"
		  * state: south
		  * Reply: 兩個圖文選單  
			* 選單1 
				title: "在台南吃吃 選個"\
				兩個按鈕: 
				1. PTT美食
				2. 別的地方好了
			* 選單2
				title: "在高雄吃吃 選個"\
				兩個按鈕: 
				1. PTT美食
				2. 別的地方好了

		* Input: 選擇按鈕 "PTT美食"
			* state: tainan, kaohsiung, taichung, changhua, taipei, taoyuan
			* Reply: 台南, 高雄, 台中, 彰化, 台北, 桃園 的批踢踢美食資訊
		
		* Input: 選擇按鈕 "別的地方好了"
			* state: eat
			* Reply: 回到eat選單
			

			