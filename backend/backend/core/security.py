from datetime import datetime, timedelta
from typing import  Union
from fastapi import HTTPException, status

import jose
from jose import JWTError
from jose import jwt
from backend.core import config as base_config


class JWTAUTH:
  @staticmethod
  def JwtEncoder(
      data: dict,
      duration: Union[timedelta, None] = None,
  ):
    access_data = data.copy()
    refresh_data = data.copy()
    if duration:
      access_data.update({"exp": datetime.utcnow() + duration})
      refresh_data.update({"exp": datetime.utcnow() + base_config.settings.REFRESH_TOKEN_EXPIRATION_DURATION})
    else:
        access_data.update({"exp": datetime.utcnow() + base_config.settings.ACCESS_TOKEN_EXPIRATION_DURATION})
        refresh_data.update({"exp": datetime.utcnow() + base_config.settings.REFRESH_TOKEN_EXPIRATION_DURATION})
    try:
      encode_jwt_refresh = jwt.encode(
          claims=refresh_data,
          key=base_config.settings.REFRESH_KEY,
          algorithm=base_config.settings.ALGORITHM,
      )
      encode_jwt_access = jwt.encode(
          claims=access_data,
          key=base_config.settings.SECRET_KEY,
          algorithm=base_config.settings.ALGORITHM,
      )
      return encode_jwt_access, encode_jwt_refresh
    except jose.JWTError as e:
      raise HTTPException(
          detail={"error": "Error jwt error"},
          status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      )


  @staticmethod
  def DataEncoder(
      data: dict,
      duration:Union[timedelta, None] = None,
      secret_key: str = None
  ):
   try:
      to_encode = data.copy()
      if duration is not None:
         to_encode.update({"exp": datetime.utcnow() + duration})
      else:
       to_encode.update({"exp": datetime.utcnow() + base_config.settings.REFRESH_TOKEN_EXPIRATION_DURATION})
      encoded_data = jwt.encode(
          claims=to_encode,
          key=secret_key if secret_key else base_config.settings.REFRESH_KEY,
          algorithm=base_config.settings.ALGORITHM,
      )
      return encoded_data
   except JWTError as e:
      raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail="Invalid token provided",
      )

  @staticmethod
  def data_decoder(encoded_data: str, secret_key: str = None):
    try:
      if secret_key is None:
        secret_key = base_config.settings.REFRESH_KEY
      elif secret_key:
        secret_key = secret_key
      
      payload = jwt.decode(
            encoded_data,
            secret_key,
            algorithms=[base_config.settings.ALGORITHM],
        )
      
      return False if not payload else payload
    except jose.JWTError:
      raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail="Invalid token provided",
      )





