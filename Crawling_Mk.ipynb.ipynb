{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from urllib.request import urlopen\n",
    "import bs4\n",
    "from urllib.parse import quote\n",
    "import csv\n",
    "\n",
    "page_num = int(input())\n",
    "all_article = []\n",
    "for i in range(1,page_num+1):\n",
    "    url = \"http://find.mk.co.kr/new/search.php?pageNum=\"+str(i)+\"&cat=&cat1=&media_eco=&pageSize=20&sub=news&dispFlag=OFF&page=news&s_kwd=%BB%EF%BC%BA%C0%FC%C0%DA&s_page=news&go_page=&ord=1&ord1=1&ord2=0&s_keyword=%BB%EF%BC%BA%C0%FC%C0%DA&period=p_direct&s_i_keyword=%BB%EF%BC%BA%C0%FC%C0%DA&s_author=&y1=2020&m1=04&d1=01&y2=2020&m2=04&d2=17&ord=0&area=ttbd\"\n",
    "    html = urlopen(url)\n",
    "    bs_obj = bs4.BeautifulSoup(html.read(),\"html.parser\")\n",
    "    span = bs_obj.findAll(\"span\",{\"class\":\"art_tit\"})\n",
    "    for a_tag in span:\n",
    "        a = a_tag.find(\"a\")\n",
    "        link = a[\"href\"]\n",
    "        if 'opinion' in link:\n",
    "            pass\n",
    "        else:\n",
    "            html2 = urlopen(link)\n",
    "            bs = bs4.BeautifulSoup(html2.read(),\"html.parser\")\n",
    "            empty =[]\n",
    "            h1 = bs.find(\"h1\",{\"class\":\"top_title\"})\n",
    "            empty.append(h1.text)#제목\n",
    "            \n",
    "            try:\n",
    "                li = bs.find(\"li\",{\"class\":\"lasttime\"})\n",
    "                empty.append(li.text[5:15]) #날짜  \n",
    "\n",
    "            except AttributeError:\n",
    "                li = bs.find(\"li\",{\"class\":\"lasttime1\"})\n",
    "                empty.append(li.text[5:15]) #날짜\n",
    "        \n",
    "            div = bs.find(\"div\",{\"class\":\"art_txt\"})\n",
    "            article = div.get_text().replace('\\r',\"\").replace('\\n','').replace('\\t','')\n",
    "            empty.append(article) #기사\n",
    "            empty.append(link) #링크\n",
    "            all_article.append(empty)\n",
    "            if li.text[5] != '2'or '[표]' in h1.text:\n",
    "                all_article.pop()\n",
    "            \n",
    "            print(link)\n",
    "    print(i)\n",
    "\n",
    "\n",
    "f = open('articles.csv','w',encoding='utf-8-sig')\n",
    "wr = csv.writer(f)\n",
    "for i in all_article:\n",
    "    if i[0] == i[2][5:len(i[0])+5]:\n",
    "        i[2] = i[2][5+len(i[0]):]\n",
    "    wr.writerow(i)\n",
    "\n",
    "f.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
