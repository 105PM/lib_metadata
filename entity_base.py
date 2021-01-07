
# -*- coding: utf-8 -*-
from .plugin import P
logger = P.logger

class EntityRatings(object):
    def __init__(self, value, max=None, votes=None, name=None, image_url=None):
        self.name = name
        self.max = max
        self.default = True
        self.value = value
        self.votes = votes
        self.image_url = image_url

    def __repr__(self):
        tmp = 'name : %s\n' % self.name
        tmp += 'value : %s\n' % self.value
        tmp += 'max : %s\n' % self.max
        return tmp


    def as_dict(self):
        return {
            'name' : self.name,
            'max' : self.max,
            'default' : self.default,
            'value' : self.value,
            'votes' : self.votes,
            'image_url' : self.image_url,
        }

class EntityThumb(object):
    def __init__(self, aspect=None, value=None):
        # banner, clearart, clearlogo, discart, landscape, poster
        self.aspect = aspect 
        self.value = value

    def as_dict(self):
        return {
            'aspect' : self.aspect,
            'value' : self.value,
        }


class EntityActor(object):
    def __init__(self, name):
        self.name = None
        self.name2 = None
        self.role = None
        self.order = None
        self.thumb = None
        self.originalname = name
        self.site = None

    def as_dict(self):
        return {
            'name' : self.name,
            'role' : self.role,
            'order' : self.order,
            'thumb' : self.thumb,
            'originalname' : self.originalname,
        }
    

class EntityExtra(object):
    def __init__(self, content_type, title, mode, content_url):
        self.content_type = content_type
        self.content_url = content_url
        self.title = title
        self.mode = mode
        

    def as_dict(self):
        return {
            'content_type' : self.content_type,
            'content_url' : self.content_url,
            'title' : self.title,
            'mode' : self.mode,
        }

class EntityMovie(object):
    # https://kodi.wiki/view/NFO_files/Movies
    def __init__(self, site, code):
        self.site = site
        self.code = code  # uniqueid

        self.title = None
        self.originaltitle = None
        self.sorttitle = None
        self.ratings = None
        self.userrating = None
        self.plot = None
        self.runtime = None
        self.thumb = None
        self.fanart = None
        self.genre = None
        self.country = None
        self.credits = None
        self.director = None
        self.premiered = None
        self.year = None
        self.studio = None
        self.trailer = None
        self.actor = None
        self.tag = None #colletion
        self.tagline = None
        self.extras = None
        self.mpaa = None
        """
        self.top250 = None
        self.outline = None
        
        """

    def __repr__(self):
        tmp = 'site : %s\n' % self.site
        tmp += 'code : %s\n' % self.code
        tmp += 'title : %s\n' % self.title
        tmp += 'originaltitle : %s\n' % self.originaltitle
        return tmp


    def as_dict(self):
        return {
            'site' : self.site,
            'code' : self.code,
            'title' : self.title,
            'originaltitle' : self.originaltitle,
            'sorttitle' : self.sorttitle,
            'ratings' : [x.as_dict() for x in self.ratings] if self.ratings is not None else None,
            'userrating' : self.userrating,
            'plot' : self.plot,
            'runtime' : self.runtime,
            'thumb' : [x.as_dict() for x in self.thumb] if self.thumb is not None else None,
            'fanart' : self.fanart,
            'genre' : self.genre,
            'country' : self.country,
            'credits' : self.credits,
            'director' : self.director,
            'premiered' : self.premiered,
            'year' : self.year,
            'studio' : self.studio,
            'trailer' : self.trailer,
            'actor' : [x.as_dict() for x in self.actor] if self.actor is not None else None,
            'tag' : self.tag,
            'tagline' : self.tagline,
            'extras' :  [x.as_dict() for x in self.extras] if self.extras is not None else None,
            'mpaa' : self.mpaa
        }





class EntitySearchItemTv(object):
    def __init__(self, site):
        self.site = site
        self.code = None
        self.title = None
        self.year = None        
        self.image_url = None        
        self.desc = None
        self.score = 0

        self.status = 1 #1:방송중, 0:방송종료, 2:방송예정
        self.extra_info = None
        self.studio = None
        self.broadcast_info = None
        self.broadcast_term = None
        self.series = None
        self.equal_name = None


    def __repr__(self):
        tmp = 'site : %s\n' % self.site
        tmp += 'code : %s\n' % self.code
        tmp += 'title : %s\n' % self.title        
        tmp += 'year : %s\n' % self.year        
        tmp += 'image_url : %s\n' % self.image_url
        tmp += 'desc : %s\n' % self.desc
        tmp += 'score : %s\n' % self.score

        tmp += 'status : %s\n' % self.status
        tmp += 'extra_info : %s\n' % self.extra_info
        tmp += 'studio : %s\n' % self.studio
        tmp += 'broadcast_info : %s\n' % self.broadcast_info
        tmp += 'broadcast_term : %s\n' % self.broadcast_term
        tmp += 'series : %s\n' % self.series

        return tmp


    def as_dict(self):
        return {
            'site' : self.site,
            'code' : self.code,
            'title' : self.title,            
            'year' : self.year,            
            'image_url' : self.image_url,
            'desc' : self.desc,            
            'score' : self.score,
            'extra_info' : self.extra_info,
            'studio' : self.studio,
            'broadcast_info' : self.broadcast_info,
            'broadcast_term' : self.broadcast_term,
            'series' : self.series,
            'equal_name' : self.equal_name,

        }
