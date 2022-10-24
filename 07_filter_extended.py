import logging 

class ContextFilter(logging.Filter):
    
    def addCtx(self, data):
        self.ip = data['ip']
        self.user = data['user']
    
    def filter(self, record : logging.LogRecord):
        if super().filter(record):
            record.ip = self.ip 
            record.user = self.user 
            
            return True 


logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(name)s - %(ip)s - %(user)s - %(message)s')

logger_a = logging.getLogger("a.b")
logger_b = logging.getLogger("a.b.c")
logger_c = logging.getLogger("d.e.f")

ctx_filter = ContextFilter("a.b")
ctx_filter.addCtx({
    'ip': "192.168.0.12",
    'user' : "Richard"
})

logger_a.addFilter(ctx_filter)
logger_b.addFilter(ctx_filter)
logger_c.addFilter(ctx_filter)

logger_a.warning("API Bookings")
logger_b.warning("API Bookings")
logger_c.warning("API Bookings")