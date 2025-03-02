from database import Base
from sqlalchemy import Column, Integer, String, DateTime
import datetime

class ErrorLog(Base):
    __tablename__ = 'error_logs'

    id = Column(Integer, primary_key=True)
    error_type = Column(String(100))
    severity = Column(String(50))
    message = Column(String(500))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String(50), default='New')

    def to_dict(self):
        return {
            'id': self.id,
            'error_type': self.error_type,
            'severity': self.severity,
            'message': self.message,
            'timestamp': self.timestamp.isoformat(),
            'status': self.status
        }
