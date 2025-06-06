# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtPositioning, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtPositioning`

import PySide6.QtPositioning
import PySide6.QtCore

import os
import enum
from typing import Any, Any, ClassVar, Dict, Dict, IO, List, List, Optional, Sequence, Tuple, Tuple, Type, Union, overload
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


NoneType: TypeAlias = type[None]


class QGeoAddress(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtPositioning.QGeoAddress) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def city(self) -> str: ...
    def clear(self) -> None: ...
    def country(self) -> str: ...
    def countryCode(self) -> str: ...
    def county(self) -> str: ...
    def district(self) -> str: ...
    def isEmpty(self) -> bool: ...
    def isTextGenerated(self) -> bool: ...
    def postalCode(self) -> str: ...
    def setCity(self, city: str) -> None: ...
    def setCountry(self, country: str) -> None: ...
    def setCountryCode(self, countryCode: str) -> None: ...
    def setCounty(self, county: str) -> None: ...
    def setDistrict(self, district: str) -> None: ...
    def setPostalCode(self, postalCode: str) -> None: ...
    def setState(self, state: str) -> None: ...
    def setStreet(self, street: str) -> None: ...
    def setStreetNumber(self, streetNumber: str) -> None: ...
    def setText(self, text: str) -> None: ...
    def state(self) -> str: ...
    def street(self) -> str: ...
    def streetNumber(self) -> str: ...
    def swap(self, other: PySide6.QtPositioning.QGeoAddress) -> None: ...
    def text(self) -> str: ...


class QGeoAreaMonitorInfo(Shiboken.Object):

    @overload
    def __init__(self, name: str = ...) -> None: ...
    @overload
    def __init__(self, other: Union[PySide6.QtPositioning.QGeoAreaMonitorInfo, str]) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(self, ds: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(self, ds: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def area(self) -> PySide6.QtPositioning.QGeoShape: ...
    def expiration(self) -> PySide6.QtCore.QDateTime: ...
    def identifier(self) -> str: ...
    def isPersistent(self) -> bool: ...
    def isValid(self) -> bool: ...
    def name(self) -> str: ...
    def notificationParameters(self) -> Dict[str, Any]: ...
    def setArea(self, newShape: PySide6.QtPositioning.QGeoShape) -> None: ...
    def setExpiration(self, expiry: PySide6.QtCore.QDateTime) -> None: ...
    def setName(self, name: str) -> None: ...
    def setNotificationParameters(self, parameters: Dict[str, Any]) -> None: ...
    def setPersistent(self, isPersistent: bool) -> None: ...
    def swap(self, other: Union[PySide6.QtPositioning.QGeoAreaMonitorInfo, str]) -> None: ...


class QGeoAreaMonitorSource(PySide6.QtCore.QObject):

    areaEntered              : ClassVar[Signal] = ... # areaEntered(QGeoAreaMonitorInfo,QGeoPositionInfo)
    areaExited               : ClassVar[Signal] = ... # areaExited(QGeoAreaMonitorInfo,QGeoPositionInfo)
    errorOccurred            : ClassVar[Signal] = ... # errorOccurred(QGeoAreaMonitorSource::Error)
    monitorExpired           : ClassVar[Signal] = ... # monitorExpired(QGeoAreaMonitorInfo)

    class AreaMonitorFeature(enum.Flag):

        AnyAreaMonitorFeature    : QGeoAreaMonitorSource.AreaMonitorFeature = ... # -0x1
        PersistentAreaMonitorFeature: QGeoAreaMonitorSource.AreaMonitorFeature = ... # 0x1

    class Error(enum.Enum):

        AccessError              : QGeoAreaMonitorSource.Error = ... # 0x0
        InsufficientPositionInfo : QGeoAreaMonitorSource.Error = ... # 0x1
        UnknownSourceError       : QGeoAreaMonitorSource.Error = ... # 0x2
        NoError                  : QGeoAreaMonitorSource.Error = ... # 0x3


    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    @overload
    def activeMonitors(self) -> List[PySide6.QtPositioning.QGeoAreaMonitorInfo]: ...
    @overload
    def activeMonitors(self, lookupArea: PySide6.QtPositioning.QGeoShape) -> List[PySide6.QtPositioning.QGeoAreaMonitorInfo]: ...
    @staticmethod
    def availableSources() -> List[str]: ...
    def backendProperty(self, name: str) -> Any: ...
    @staticmethod
    def createDefaultSource(parent: PySide6.QtCore.QObject) -> PySide6.QtPositioning.QGeoAreaMonitorSource: ...
    @staticmethod
    def createSource(sourceName: str, parent: PySide6.QtCore.QObject) -> PySide6.QtPositioning.QGeoAreaMonitorSource: ...
    def error(self) -> PySide6.QtPositioning.QGeoAreaMonitorSource.Error: ...
    def positionInfoSource(self) -> PySide6.QtPositioning.QGeoPositionInfoSource: ...
    def requestUpdate(self, monitor: Union[PySide6.QtPositioning.QGeoAreaMonitorInfo, str], signal: Union[bytes, bytearray, memoryview]) -> bool: ...
    def setBackendProperty(self, name: str, value: Any) -> bool: ...
    def setPositionInfoSource(self, source: PySide6.QtPositioning.QGeoPositionInfoSource) -> None: ...
    def sourceName(self) -> str: ...
    def startMonitoring(self, monitor: Union[PySide6.QtPositioning.QGeoAreaMonitorInfo, str]) -> bool: ...
    def stopMonitoring(self, monitor: Union[PySide6.QtPositioning.QGeoAreaMonitorInfo, str]) -> bool: ...
    def supportedAreaMonitorFeatures(self) -> PySide6.QtPositioning.QGeoAreaMonitorSource.AreaMonitorFeature: ...


class QGeoCircle(PySide6.QtPositioning.QGeoShape):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, center: PySide6.QtPositioning.QGeoCoordinate, radius: float = ...) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtPositioning.QGeoShape) -> None: ...
    @overload
    def __init__(self, other: Union[PySide6.QtPositioning.QGeoCircle, PySide6.QtPositioning.QGeoCoordinate, PySide6.QtPositioning.QGeoShape]) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def center(self) -> PySide6.QtPositioning.QGeoCoordinate: ...
    def extendCircle(self, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def radius(self) -> float: ...
    def setCenter(self, center: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def setRadius(self, radius: float) -> None: ...
    def toString(self) -> str: ...
    def translate(self, degreesLatitude: float, degreesLongitude: float) -> None: ...
    def translated(self, degreesLatitude: float, degreesLongitude: float) -> PySide6.QtPositioning.QGeoCircle: ...


class QGeoCoordinate(Shiboken.Object):

    class CoordinateFormat(enum.Enum):

        Degrees                  : QGeoCoordinate.CoordinateFormat = ... # 0x0
        DegreesWithHemisphere    : QGeoCoordinate.CoordinateFormat = ... # 0x1
        DegreesMinutes           : QGeoCoordinate.CoordinateFormat = ... # 0x2
        DegreesMinutesWithHemisphere: QGeoCoordinate.CoordinateFormat = ... # 0x3
        DegreesMinutesSeconds    : QGeoCoordinate.CoordinateFormat = ... # 0x4
        DegreesMinutesSecondsWithHemisphere: QGeoCoordinate.CoordinateFormat = ... # 0x5

    class CoordinateType(enum.Enum):

        InvalidCoordinate        : QGeoCoordinate.CoordinateType = ... # 0x0
        Coordinate2D             : QGeoCoordinate.CoordinateType = ... # 0x1
        Coordinate3D             : QGeoCoordinate.CoordinateType = ... # 0x2


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, latitude: float, longitude: float) -> None: ...
    @overload
    def __init__(self, latitude: float, longitude: float, altitude: float) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtPositioning.QGeoCoordinate) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def altitude(self) -> float: ...
    def atDistanceAndAzimuth(self, distance: float, azimuth: float, distanceUp: float = ...) -> PySide6.QtPositioning.QGeoCoordinate: ...
    def azimuthTo(self, other: PySide6.QtPositioning.QGeoCoordinate) -> float: ...
    def distanceTo(self, other: PySide6.QtPositioning.QGeoCoordinate) -> float: ...
    def isValid(self) -> bool: ...
    def latitude(self) -> float: ...
    def longitude(self) -> float: ...
    def setAltitude(self, altitude: float) -> None: ...
    def setLatitude(self, latitude: float) -> None: ...
    def setLongitude(self, longitude: float) -> None: ...
    def swap(self, other: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def toString(self, format: PySide6.QtPositioning.QGeoCoordinate.CoordinateFormat = ...) -> str: ...
    def type(self) -> PySide6.QtPositioning.QGeoCoordinate.CoordinateType: ...


class QGeoLocation(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtPositioning.QGeoLocation) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def address(self) -> PySide6.QtPositioning.QGeoAddress: ...
    def boundingShape(self) -> PySide6.QtPositioning.QGeoShape: ...
    def coordinate(self) -> PySide6.QtPositioning.QGeoCoordinate: ...
    def extendedAttributes(self) -> Dict[str, Any]: ...
    def isEmpty(self) -> bool: ...
    def setAddress(self, address: PySide6.QtPositioning.QGeoAddress) -> None: ...
    def setBoundingShape(self, shape: PySide6.QtPositioning.QGeoShape) -> None: ...
    def setCoordinate(self, position: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def setExtendedAttributes(self, data: Dict[str, Any]) -> None: ...
    def swap(self, other: PySide6.QtPositioning.QGeoLocation) -> None: ...


class QGeoPath(PySide6.QtPositioning.QGeoShape):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtPositioning.QGeoShape) -> None: ...
    @overload
    def __init__(self, other: Union[PySide6.QtPositioning.QGeoPath, PySide6.QtPositioning.QGeoShape, Sequence[PySide6.QtPositioning.QGeoCoordinate]]) -> None: ...
    @overload
    def __init__(self, path: Sequence[PySide6.QtPositioning.QGeoCoordinate], width: float = ...) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def addCoordinate(self, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def clearPath(self) -> None: ...
    def containsCoordinate(self, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> bool: ...
    def coordinateAt(self, index: int) -> PySide6.QtPositioning.QGeoCoordinate: ...
    def insertCoordinate(self, index: int, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def length(self, indexFrom: int = ..., indexTo: int = ...) -> float: ...
    def path(self) -> List[PySide6.QtPositioning.QGeoCoordinate]: ...
    @overload
    def removeCoordinate(self, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    @overload
    def removeCoordinate(self, index: int) -> None: ...
    def replaceCoordinate(self, index: int, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def setPath(self, path: Sequence[PySide6.QtPositioning.QGeoCoordinate]) -> None: ...
    def setVariantPath(self, path: Sequence[Any]) -> None: ...
    def setWidth(self, width: float) -> None: ...
    def size(self) -> int: ...
    def toString(self) -> str: ...
    def translate(self, degreesLatitude: float, degreesLongitude: float) -> None: ...
    def translated(self, degreesLatitude: float, degreesLongitude: float) -> PySide6.QtPositioning.QGeoPath: ...
    def variantPath(self) -> List[Any]: ...
    def width(self) -> float: ...


class QGeoPolygon(PySide6.QtPositioning.QGeoShape):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtPositioning.QGeoShape) -> None: ...
    @overload
    def __init__(self, other: Union[PySide6.QtPositioning.QGeoPolygon, PySide6.QtPositioning.QGeoShape, Sequence[PySide6.QtPositioning.QGeoCoordinate]]) -> None: ...
    @overload
    def __init__(self, path: Sequence[PySide6.QtPositioning.QGeoCoordinate]) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def addCoordinate(self, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    @overload
    def addHole(self, holePath: Sequence[PySide6.QtPositioning.QGeoCoordinate]) -> None: ...
    @overload
    def addHole(self, holePath: Any) -> None: ...
    def containsCoordinate(self, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> bool: ...
    def coordinateAt(self, index: int) -> PySide6.QtPositioning.QGeoCoordinate: ...
    def hole(self, index: int) -> List[Any]: ...
    def holePath(self, index: int) -> List[PySide6.QtPositioning.QGeoCoordinate]: ...
    def holesCount(self) -> int: ...
    def insertCoordinate(self, index: int, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def length(self, indexFrom: int = ..., indexTo: int = ...) -> float: ...
    def perimeter(self) -> List[PySide6.QtPositioning.QGeoCoordinate]: ...
    @overload
    def removeCoordinate(self, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    @overload
    def removeCoordinate(self, index: int) -> None: ...
    def removeHole(self, index: int) -> None: ...
    def replaceCoordinate(self, index: int, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def setPerimeter(self, path: Sequence[PySide6.QtPositioning.QGeoCoordinate]) -> None: ...
    def size(self) -> int: ...
    def toString(self) -> str: ...
    def translate(self, degreesLatitude: float, degreesLongitude: float) -> None: ...
    def translated(self, degreesLatitude: float, degreesLongitude: float) -> PySide6.QtPositioning.QGeoPolygon: ...


class QGeoPositionInfo(Shiboken.Object):

    class Attribute(enum.Enum):

        Direction                : QGeoPositionInfo.Attribute = ... # 0x0
        GroundSpeed              : QGeoPositionInfo.Attribute = ... # 0x1
        VerticalSpeed            : QGeoPositionInfo.Attribute = ... # 0x2
        MagneticVariation        : QGeoPositionInfo.Attribute = ... # 0x3
        HorizontalAccuracy       : QGeoPositionInfo.Attribute = ... # 0x4
        VerticalAccuracy         : QGeoPositionInfo.Attribute = ... # 0x5
        DirectionAccuracy        : QGeoPositionInfo.Attribute = ... # 0x6


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, coordinate: PySide6.QtPositioning.QGeoCoordinate, updateTime: PySide6.QtCore.QDateTime) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtPositioning.QGeoPositionInfo) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def attribute(self, attribute: PySide6.QtPositioning.QGeoPositionInfo.Attribute) -> float: ...
    def coordinate(self) -> PySide6.QtPositioning.QGeoCoordinate: ...
    def hasAttribute(self, attribute: PySide6.QtPositioning.QGeoPositionInfo.Attribute) -> bool: ...
    def isValid(self) -> bool: ...
    def removeAttribute(self, attribute: PySide6.QtPositioning.QGeoPositionInfo.Attribute) -> None: ...
    def setAttribute(self, attribute: PySide6.QtPositioning.QGeoPositionInfo.Attribute, value: float) -> None: ...
    def setCoordinate(self, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def setTimestamp(self, timestamp: PySide6.QtCore.QDateTime) -> None: ...
    def swap(self, other: PySide6.QtPositioning.QGeoPositionInfo) -> None: ...
    def timestamp(self) -> PySide6.QtCore.QDateTime: ...


class QGeoPositionInfoSource(PySide6.QtCore.QObject):

    errorOccurred            : ClassVar[Signal] = ... # errorOccurred(QGeoPositionInfoSource::Error)
    positionUpdated          : ClassVar[Signal] = ... # positionUpdated(QGeoPositionInfo)
    supportedPositioningMethodsChanged: ClassVar[Signal] = ... # supportedPositioningMethodsChanged()

    class Error(enum.Enum):

        AccessError              : QGeoPositionInfoSource.Error = ... # 0x0
        ClosedError              : QGeoPositionInfoSource.Error = ... # 0x1
        UnknownSourceError       : QGeoPositionInfoSource.Error = ... # 0x2
        NoError                  : QGeoPositionInfoSource.Error = ... # 0x3
        UpdateTimeoutError       : QGeoPositionInfoSource.Error = ... # 0x4

    class PositioningMethod(enum.Flag):

        NonSatellitePositioningMethods: QGeoPositionInfoSource.PositioningMethod = ... # -0x100
        AllPositioningMethods    : QGeoPositionInfoSource.PositioningMethod = ... # -0x1
        NoPositioningMethods     : QGeoPositionInfoSource.PositioningMethod = ... # 0x0
        SatellitePositioningMethods: QGeoPositionInfoSource.PositioningMethod = ... # 0xff


    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    @staticmethod
    def availableSources() -> List[str]: ...
    def backendProperty(self, name: str) -> Any: ...
    @overload
    @staticmethod
    def createDefaultSource(parameters: Dict[str, Any], parent: PySide6.QtCore.QObject) -> PySide6.QtPositioning.QGeoPositionInfoSource: ...
    @overload
    @staticmethod
    def createDefaultSource(parent: PySide6.QtCore.QObject) -> PySide6.QtPositioning.QGeoPositionInfoSource: ...
    @overload
    @staticmethod
    def createSource(sourceName: str, parameters: Dict[str, Any], parent: PySide6.QtCore.QObject) -> PySide6.QtPositioning.QGeoPositionInfoSource: ...
    @overload
    @staticmethod
    def createSource(sourceName: str, parent: PySide6.QtCore.QObject) -> PySide6.QtPositioning.QGeoPositionInfoSource: ...
    def error(self) -> PySide6.QtPositioning.QGeoPositionInfoSource.Error: ...
    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly: bool = ...) -> PySide6.QtPositioning.QGeoPositionInfo: ...
    def minimumUpdateInterval(self) -> int: ...
    def preferredPositioningMethods(self) -> PySide6.QtPositioning.QGeoPositionInfoSource.PositioningMethod: ...
    def requestUpdate(self, timeout: int = ...) -> None: ...
    def setBackendProperty(self, name: str, value: Any) -> bool: ...
    def setPreferredPositioningMethods(self, methods: PySide6.QtPositioning.QGeoPositionInfoSource.PositioningMethod) -> None: ...
    def setUpdateInterval(self, msec: int) -> None: ...
    def sourceName(self) -> str: ...
    def startUpdates(self) -> None: ...
    def stopUpdates(self) -> None: ...
    def supportedPositioningMethods(self) -> PySide6.QtPositioning.QGeoPositionInfoSource.PositioningMethod: ...
    def updateInterval(self) -> int: ...


class QGeoPositionInfoSourceFactory(Shiboken.Object):

    def __init__(self) -> None: ...

    def areaMonitor(self, parent: PySide6.QtCore.QObject, parameters: Dict[str, Any]) -> PySide6.QtPositioning.QGeoAreaMonitorSource: ...
    def positionInfoSource(self, parent: PySide6.QtCore.QObject, parameters: Dict[str, Any]) -> PySide6.QtPositioning.QGeoPositionInfoSource: ...
    def satelliteInfoSource(self, parent: PySide6.QtCore.QObject, parameters: Dict[str, Any]) -> PySide6.QtPositioning.QGeoSatelliteInfoSource: ...


class QGeoRectangle(PySide6.QtPositioning.QGeoShape):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, center: PySide6.QtPositioning.QGeoCoordinate, degreesWidth: float, degreesHeight: float) -> None: ...
    @overload
    def __init__(self, coordinates: Sequence[PySide6.QtPositioning.QGeoCoordinate]) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtPositioning.QGeoShape) -> None: ...
    @overload
    def __init__(self, other: Union[PySide6.QtPositioning.QGeoRectangle, PySide6.QtPositioning.QGeoShape, Sequence[PySide6.QtPositioning.QGeoCoordinate]]) -> None: ...
    @overload
    def __init__(self, topLeft: PySide6.QtPositioning.QGeoCoordinate, bottomRight: PySide6.QtPositioning.QGeoCoordinate) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def __ior__(self, rectangle: Union[PySide6.QtPositioning.QGeoRectangle, PySide6.QtPositioning.QGeoShape, Sequence[PySide6.QtPositioning.QGeoCoordinate]]) -> PySide6.QtPositioning.QGeoRectangle: ...
    def __lshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def __or__(self, rectangle: Union[PySide6.QtPositioning.QGeoRectangle, PySide6.QtPositioning.QGeoShape, Sequence[PySide6.QtPositioning.QGeoCoordinate]]) -> PySide6.QtPositioning.QGeoRectangle: ...
    def __rshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def bottomLeft(self) -> PySide6.QtPositioning.QGeoCoordinate: ...
    def bottomRight(self) -> PySide6.QtPositioning.QGeoCoordinate: ...
    def center(self) -> PySide6.QtPositioning.QGeoCoordinate: ...
    @overload
    def contains(self, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> bool: ...
    @overload
    def contains(self, rectangle: Union[PySide6.QtPositioning.QGeoRectangle, PySide6.QtPositioning.QGeoShape, Sequence[PySide6.QtPositioning.QGeoCoordinate]]) -> bool: ...
    def extendRectangle(self, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def height(self) -> float: ...
    def intersects(self, rectangle: Union[PySide6.QtPositioning.QGeoRectangle, PySide6.QtPositioning.QGeoShape, Sequence[PySide6.QtPositioning.QGeoCoordinate]]) -> bool: ...
    def setBottomLeft(self, bottomLeft: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def setBottomRight(self, bottomRight: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def setCenter(self, center: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def setHeight(self, degreesHeight: float) -> None: ...
    def setTopLeft(self, topLeft: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def setTopRight(self, topRight: PySide6.QtPositioning.QGeoCoordinate) -> None: ...
    def setWidth(self, degreesWidth: float) -> None: ...
    def toString(self) -> str: ...
    def topLeft(self) -> PySide6.QtPositioning.QGeoCoordinate: ...
    def topRight(self) -> PySide6.QtPositioning.QGeoCoordinate: ...
    def translate(self, degreesLatitude: float, degreesLongitude: float) -> None: ...
    def translated(self, degreesLatitude: float, degreesLongitude: float) -> PySide6.QtPositioning.QGeoRectangle: ...
    def united(self, rectangle: Union[PySide6.QtPositioning.QGeoRectangle, PySide6.QtPositioning.QGeoShape, Sequence[PySide6.QtPositioning.QGeoCoordinate]]) -> PySide6.QtPositioning.QGeoRectangle: ...
    def width(self) -> float: ...


class QGeoSatelliteInfo(Shiboken.Object):

    class Attribute(enum.Enum):

        Elevation                : QGeoSatelliteInfo.Attribute = ... # 0x0
        Azimuth                  : QGeoSatelliteInfo.Attribute = ... # 0x1

    class SatelliteSystem(enum.Enum):

        Undefined                : QGeoSatelliteInfo.SatelliteSystem = ... # 0x0
        GPS                      : QGeoSatelliteInfo.SatelliteSystem = ... # 0x1
        GLONASS                  : QGeoSatelliteInfo.SatelliteSystem = ... # 0x2
        GALILEO                  : QGeoSatelliteInfo.SatelliteSystem = ... # 0x3
        BEIDOU                   : QGeoSatelliteInfo.SatelliteSystem = ... # 0x4
        QZSS                     : QGeoSatelliteInfo.SatelliteSystem = ... # 0x5
        Multiple                 : QGeoSatelliteInfo.SatelliteSystem = ... # 0xff
        CustomType               : QGeoSatelliteInfo.SatelliteSystem = ... # 0x100


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtPositioning.QGeoSatelliteInfo) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def attribute(self, attribute: PySide6.QtPositioning.QGeoSatelliteInfo.Attribute) -> float: ...
    def hasAttribute(self, attribute: PySide6.QtPositioning.QGeoSatelliteInfo.Attribute) -> bool: ...
    def removeAttribute(self, attribute: PySide6.QtPositioning.QGeoSatelliteInfo.Attribute) -> None: ...
    def satelliteIdentifier(self) -> int: ...
    def satelliteSystem(self) -> PySide6.QtPositioning.QGeoSatelliteInfo.SatelliteSystem: ...
    def setAttribute(self, attribute: PySide6.QtPositioning.QGeoSatelliteInfo.Attribute, value: float) -> None: ...
    def setSatelliteIdentifier(self, satId: int) -> None: ...
    def setSatelliteSystem(self, system: PySide6.QtPositioning.QGeoSatelliteInfo.SatelliteSystem) -> None: ...
    def setSignalStrength(self, signalStrength: int) -> None: ...
    def signalStrength(self) -> int: ...
    def swap(self, other: PySide6.QtPositioning.QGeoSatelliteInfo) -> None: ...


class QGeoSatelliteInfoSource(PySide6.QtCore.QObject):

    errorOccurred            : ClassVar[Signal] = ... # errorOccurred(QGeoSatelliteInfoSource::Error)
    satellitesInUseUpdated   : ClassVar[Signal] = ... # satellitesInUseUpdated(QList<QGeoSatelliteInfo>)
    satellitesInViewUpdated  : ClassVar[Signal] = ... # satellitesInViewUpdated(QList<QGeoSatelliteInfo>)

    class Error(enum.Enum):

        UnknownSourceError       : QGeoSatelliteInfoSource.Error = ... # -0x1
        AccessError              : QGeoSatelliteInfoSource.Error = ... # 0x0
        ClosedError              : QGeoSatelliteInfoSource.Error = ... # 0x1
        NoError                  : QGeoSatelliteInfoSource.Error = ... # 0x2
        UpdateTimeoutError       : QGeoSatelliteInfoSource.Error = ... # 0x3


    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...

    @staticmethod
    def availableSources() -> List[str]: ...
    def backendProperty(self, name: str) -> Any: ...
    @overload
    @staticmethod
    def createDefaultSource(parameters: Dict[str, Any], parent: PySide6.QtCore.QObject) -> PySide6.QtPositioning.QGeoSatelliteInfoSource: ...
    @overload
    @staticmethod
    def createDefaultSource(parent: PySide6.QtCore.QObject) -> PySide6.QtPositioning.QGeoSatelliteInfoSource: ...
    @overload
    @staticmethod
    def createSource(sourceName: str, parameters: Dict[str, Any], parent: PySide6.QtCore.QObject) -> PySide6.QtPositioning.QGeoSatelliteInfoSource: ...
    @overload
    @staticmethod
    def createSource(sourceName: str, parent: PySide6.QtCore.QObject) -> PySide6.QtPositioning.QGeoSatelliteInfoSource: ...
    def error(self) -> PySide6.QtPositioning.QGeoSatelliteInfoSource.Error: ...
    def minimumUpdateInterval(self) -> int: ...
    def requestUpdate(self, timeout: int = ...) -> None: ...
    def setBackendProperty(self, name: str, value: Any) -> bool: ...
    def setUpdateInterval(self, msec: int) -> None: ...
    def sourceName(self) -> str: ...
    def startUpdates(self) -> None: ...
    def stopUpdates(self) -> None: ...
    def updateInterval(self) -> int: ...


class QGeoShape(Shiboken.Object):

    class ShapeType(enum.Enum):

        UnknownType              : QGeoShape.ShapeType = ... # 0x0
        RectangleType            : QGeoShape.ShapeType = ... # 0x1
        CircleType               : QGeoShape.ShapeType = ... # 0x2
        PathType                 : QGeoShape.ShapeType = ... # 0x3
        PolygonType              : QGeoShape.ShapeType = ... # 0x4


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PySide6.QtPositioning.QGeoShape) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(self, stream: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def boundingGeoRectangle(self) -> PySide6.QtPositioning.QGeoRectangle: ...
    def center(self) -> PySide6.QtPositioning.QGeoCoordinate: ...
    def contains(self, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> bool: ...
    def isEmpty(self) -> bool: ...
    def isValid(self) -> bool: ...
    def toString(self) -> str: ...
    def type(self) -> PySide6.QtPositioning.QGeoShape.ShapeType: ...


class QIntList(object): ...


class QNmeaPositionInfoSource(PySide6.QtPositioning.QGeoPositionInfoSource):

    class UpdateMode(enum.Enum):

        RealTimeMode             : QNmeaPositionInfoSource.UpdateMode = ... # 0x1
        SimulationMode           : QNmeaPositionInfoSource.UpdateMode = ... # 0x2


    def __init__(self, updateMode: PySide6.QtPositioning.QNmeaPositionInfoSource.UpdateMode, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def device(self) -> PySide6.QtCore.QIODevice: ...
    def error(self) -> PySide6.QtPositioning.QGeoPositionInfoSource.Error: ...
    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly: bool = ...) -> PySide6.QtPositioning.QGeoPositionInfo: ...
    def minimumUpdateInterval(self) -> int: ...
    @overload
    def parsePosInfoFromNmeaData(self, data: Union[bytes, bytearray, memoryview], size: int, posInfo: PySide6.QtPositioning.QGeoPositionInfo) -> Tuple[bool, bool]: ...
    @overload
    def parsePosInfoFromNmeaData(self, data: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview], posInfo: PySide6.QtPositioning.QGeoPositionInfo) -> Tuple[bool, bool]: ...
    def requestUpdate(self, timeout: int = ...) -> None: ...
    def setDevice(self, source: PySide6.QtCore.QIODevice) -> None: ...
    def setError(self, positionError: PySide6.QtPositioning.QGeoPositionInfoSource.Error) -> None: ...
    def setUpdateInterval(self, msec: int) -> None: ...
    def setUserEquivalentRangeError(self, uere: float) -> None: ...
    def startUpdates(self) -> None: ...
    def stopUpdates(self) -> None: ...
    def supportedPositioningMethods(self) -> PySide6.QtPositioning.QGeoPositionInfoSource.PositioningMethod: ...
    def updateMode(self) -> PySide6.QtPositioning.QNmeaPositionInfoSource.UpdateMode: ...
    def userEquivalentRangeError(self) -> float: ...


class QNmeaSatelliteInfoSource(PySide6.QtPositioning.QGeoSatelliteInfoSource):

    class SatelliteInfoParseStatus(enum.Enum):

        NotParsed                : QNmeaSatelliteInfoSource.SatelliteInfoParseStatus = ... # 0x0
        PartiallyParsed          : QNmeaSatelliteInfoSource.SatelliteInfoParseStatus = ... # 0x1
        FullyParsed              : QNmeaSatelliteInfoSource.SatelliteInfoParseStatus = ... # 0x2

    class UpdateMode(enum.Enum):

        RealTimeMode             : QNmeaSatelliteInfoSource.UpdateMode = ... # 0x1
        SimulationMode           : QNmeaSatelliteInfoSource.UpdateMode = ... # 0x2


    def __init__(self, mode: PySide6.QtPositioning.QNmeaSatelliteInfoSource.UpdateMode, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

    def backendProperty(self, name: str) -> Any: ...
    def device(self) -> PySide6.QtCore.QIODevice: ...
    def error(self) -> PySide6.QtPositioning.QGeoSatelliteInfoSource.Error: ...
    def minimumUpdateInterval(self) -> int: ...
    @overload
    def parseSatelliteInfoFromNmea(self, data: Union[bytes, bytearray, memoryview], size: int, infos: Sequence[PySide6.QtPositioning.QGeoSatelliteInfo], system: PySide6.QtPositioning.QGeoSatelliteInfo.SatelliteSystem) -> PySide6.QtPositioning.QNmeaSatelliteInfoSource.SatelliteInfoParseStatus: ...
    @overload
    def parseSatelliteInfoFromNmea(self, data: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview], infos: Sequence[PySide6.QtPositioning.QGeoSatelliteInfo], system: PySide6.QtPositioning.QGeoSatelliteInfo.SatelliteSystem) -> PySide6.QtPositioning.QNmeaSatelliteInfoSource.SatelliteInfoParseStatus: ...
    @overload
    def parseSatellitesInUseFromNmea(self, data: Union[bytes, bytearray, memoryview], size: int, pnrsInUse: Sequence[int]) -> PySide6.QtPositioning.QGeoSatelliteInfo.SatelliteSystem: ...
    @overload
    def parseSatellitesInUseFromNmea(self, data: Union[PySide6.QtCore.QByteArray, bytes, bytearray, memoryview], pnrsInUse: Sequence[int]) -> PySide6.QtPositioning.QGeoSatelliteInfo.SatelliteSystem: ...
    def requestUpdate(self, timeout: int = ...) -> None: ...
    def setBackendProperty(self, name: str, value: Any) -> bool: ...
    def setDevice(self, source: PySide6.QtCore.QIODevice) -> None: ...
    def setError(self, satelliteError: PySide6.QtPositioning.QGeoSatelliteInfoSource.Error) -> None: ...
    def setUpdateInterval(self, msec: int) -> None: ...
    def startUpdates(self) -> None: ...
    def stopUpdates(self) -> None: ...
    def updateMode(self) -> PySide6.QtPositioning.QNmeaSatelliteInfoSource.UpdateMode: ...


# eof
