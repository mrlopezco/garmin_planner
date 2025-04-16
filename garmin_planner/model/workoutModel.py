from garmin_planner.constant import (
    SportType,
    DistanceUnit,
    StepType,
    ConditionType,
    TargetType,
)
from dataclasses import dataclass
from typing import Optional, List, Union


@dataclass
class WorkoutStep:
    stepId: int
    stepOrder: int
    stepType: StepType
    endCondition: ConditionType
    endConditionValue: int
    preferredEndConditionUnit: Optional[DistanceUnit] = (
        None  # this when end con is distance
    )
    type: str = "ExecutableStepDTO"
    targetType: Optional[TargetType] = None
    targetValueOne: Optional[float] = None  # when its custom
    targetValueTwo: Optional[float] = None  # when its custom
    zoneNumber: Optional[int] = None  # This needed when target = zone based
    targetValueUnit: Optional[str] = None
    stepAudioNote: Optional[str] = None


@dataclass
class RepeatStep:
    stepId: int
    stepOrder: int
    numberOfIterations: int
    workoutSteps: List[WorkoutStep]  # can be nested repeat
    stepType: StepType = StepType.REPEAT
    smartRepeat: bool = False
    childStepId: int = (
        1  # havent figure out this, it seems all its child step need this
    )
    type: str = "RepeatGroupDTO"
    skipLastRestStep: bool = False
    endCondition: ConditionType = ConditionType.ITERATION_ENDS


@dataclass
class WorkoutSegment:
    segmentOrder: int
    sportType: SportType
    workoutSteps: List[WorkoutStep | RepeatStep]


@dataclass
class WorkoutModel:
    workoutName: str
    sportType: SportType
    workoutSegments: List[WorkoutSegment]
    subSportType: Optional[str] = None
    avgTrainingSpeed: Optional[float] = None
    estimatedDistanceUnit: Optional[DistanceUnit] = DistanceUnit.NONE
    estimatedDurationInSecs: Optional[int] = 0
    estimatedDistanceInMeters: Optional[float] = 0
    estimateType: Optional[str] = None
    isWheelchair: Optional[bool] = False
