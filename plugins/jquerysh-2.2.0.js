/**
 * jQuery-like interfaces v2.2.0
 * http://rightjs.org/plugins/jquerysh
 *
 * Copyright (C) 2009-2011 Nikolay Nemshilov
 */
(function(a){function l(a,b,c,d){typeof b==="function"&&(d=c,c=b,b=undefined);return{url:a,data:b,success:c,dataType:d}}function k(a,b){return j.ajax(f(l.apply(this,b),a))}var b=a.$,c=a.$$,d=a.$E,e=a.$A,f=a.$ext,g=a.Xhr,h=a.Browser,i=a.Object;a.jQuerysh={version:"2.2.0",collectionMethods:{live:function(a,b){this.cssRule.on(a,b);return this},die:function(a,b){this.cssRule.stopObserving(a,b);return this}}};var j=function(e){switch(typeof e){case"string":var g=e[0],h=e.substr(1);if(g==="#"&&/^[\w\-]+$/.test(h))return b(h);if(g==="<")return d("div",{html:e}).first();g=c(e),g.cssRule=a(e);return f(g,a.jQuerysh.collectionMethods);case"function":return b(document).onReady(e);default:return b(e)}};f(j,{browser:{webkit:h.WebKit,opera:h.Opera,msie:h.IE,mozilla:h.Gecko},isFunction:function(b){return a.isFunction(b)},isArray:function(b){return a.isArray(b)},isPlainObject:function(b){return a.isHash(b)},isEmptyObject:function(a){return i.empty(a)},globalEval:function(b){return a.$eval(b)},makeArray:function(a){return e(a)},each:function(a,b){return e(a,function(a,c){b(c,a)})},map:function(a){return e(value).map(a)},unique:function(a){return e(a).uniq()},merge:function(a,b){return e(a).merge(b)},extend:function(){return i.merge.apply(i,arguments)},proxy:function(b,c){return a(b).bind(c)},noop:function(){return a(function(){})}}),a.Element.include({appendTo:function(a){return this.insertTo(a)},prepend:function(a){return this.insert(a,"top")},before:function(a){return this.insert(a,"before")},after:function(a){return this.insert(a,"after")},insertBefore:function(a){return this.insertTo(a,"before")},attr:function(a,b){return b===undefined?this.get(a):this.set(a,b)},css:function(a,b){return typeof a==="string"&&b===undefined?this.getStyle(a):this.setStyle(a,b)},offset:function(){var a=this.position();return{left:a.x,top:a.y}},width:function(){return this.size().x},height:function(){return this.size().y},scrollLeft:function(){return this.scrolls().x},scrollTop:function(){return this.scrolls().y},bind:function(){return this.on.apply(this,arguments)},unbind:function(){return this.stopObserving.apply(this,arguments)},trigger:function(a,b){return this.fire(a,b)},animate:function(a,b,c){return this.morph(a,{duration:b,onFinish:c})},fadeIn:function(){return this.fade("in")},fadeOut:function(){return this.fade("out")},slideIn:function(){return this.slide("in")},slideOut:function(){return this.slide("out")}}),f(j,{param:function(a){return i.toQueryString(a)},ajax:function(a,b){function d(a,c){a(b.dataType==="json"?c.json:c.text,c.successful()?"success":"error",c)}b=b||{},typeof a==="string"?b.url=a:b=a;var c={};b.success&&(c.onSuccess=function(){d(b.success,this)}),b.error&&(c.onFailure=function(){d(b.error,this)}),b.complete&&(c.onComplete=function(){d(b.complete,this)}),c.method=b.type,b.headers&&(c.headers=b.headers),b.jsonp&&(c.jsonp=b.jsonp),b.url.indexOf("callback=?")>0&&(c.jsonp=!0,b.url=b.url.replace(/(\?|\&)callback=\?/,""));return(new g(b.url,c)).send(b.data)},get:function(){return k({type:"get"},arguments)},post:function(a,b,c,d){return k({type:"post"},arguments)},getJSON:function(a,b,c){return k({dataType:"json"},arguments)},getScript:function(a,b){return k({dataType:"script"},arguments)}}),g.include({success:function(a){return this.on("success",a)},error:function(a){return this.on("failure",a)},complete:function(a){return this.on("complete",a)}}),window.$=window.jQuery=j})(RightJS)