import time

from .plugin import P
from .site_util import SiteUtil

logger = P.logger

# 사이트 차단


class SiteAvdbs:
    site_char = "A"

    @staticmethod
    def __get_actor_info(originalname, proxy_url=None):
        url = "https://www.avdbs.com/w2017/api/iux_kwd_srch_log.php"
        params = {"op": "srch", "kwd": originalname}
        seq = SiteUtil.get_response(url, params=params, proxy_url=proxy_url, timeout=5).json()["seq"]
        url = "https://www.avdbs.com/w2017/page/search/search_actor.php"
        params = {"kwd": originalname, "seq": seq}
        tree = SiteUtil.get_tree(url, params=params, proxy_url=proxy_url, timeout=5)

        img_src = tree.xpath(".//img/@src")
        if not img_src:
            logger.debug("검색 결과 없음: originalname=%s", originalname)
            return None

        names = tree.xpath('//p[starts-with(@class, "e_name")]/a')[0].text_content()
        names = names.strip(")").split("(")
        if len(names) != 2:
            logger.debug("검색 결과에서 이름을 찾을 수 없음: len(%s) != 2", names)
            return None

        name_en, name_ja = [x.strip() for x in names]
        if name_ja == originalname:
            name_ko = tree.xpath('//p[starts-with(@class, "k_name")]/a')[0].text_content().strip()
            return {
                "name": name_ko,
                "name2": name_en,
                "site": "avdbs",
                "thumb": SiteUtil.process_image_mode("3", img_src[0], proxy_url=proxy_url),
            }
        logger.debug("검색 결과 중 일치 항목 없음: %s != %s", name_ja, originalname)
        return None

    @staticmethod
    def get_actor_info(entity_actor, proxy_url=None, retry=True):
        try:
            info = SiteAvdbs.__get_actor_info(entity_actor["originalname"], proxy_url=proxy_url)
        except Exception:
            # 2020-06-01
            # 단시간에 많은 요청시 Error발생
            if retry:
                logger.debug("단시간 많은 요청으로 재시도")
                time.sleep(2)
                return SiteAvdbs.get_actor_info(entity_actor, proxy_url=proxy_url, retry=False)
            logger.exception("배우 정보 업데이트 중 예외: originalname=%s", entity_actor["originalname"])
        else:
            if info is not None:
                entity_actor.update(info)
        return entity_actor
