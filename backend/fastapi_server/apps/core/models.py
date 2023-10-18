from sqlalchemy import Column, DateTime, func, String


class AuditModelMixin(object):
    created_by = Column(String, nullable=True)
    updated_by = Column(String, nullable=True)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), onupdate=func.now())
