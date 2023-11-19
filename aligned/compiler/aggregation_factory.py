from dataclasses import dataclass
from datetime import timedelta

from aligned.compiler.feature_factory import (
    AggregationTransformationFactory,
    FeatureFactory,
    FeatureReferance,
    String,
    TransformationFactory,
)
from aligned.schemas.derivied_feature import AggregateOver, AggregationTimeWindow, DerivedFeature
from aligned.schemas.transformation import Transformation


def aggregate_over(
    group_by: list[FeatureReferance],
    time_column: FeatureReferance | None,
    time_window: timedelta | None,
    every_interval: timedelta | None,
    condition: DerivedFeature | None,
) -> AggregateOver:
    if not time_window:
        return AggregateOver(group_by)

    if not time_column:
        raise ValueError(
            f'Aggregation {group_by} over {time_column} have a time window, but no event timestamp to use'
        )

    return AggregateOver(
        group_by, AggregationTimeWindow(time_window, time_column, every_interval), condition=condition
    )


@dataclass
class ConcatStringsAggrigationFactory(TransformationFactory, AggregationTransformationFactory):

    feature: String
    separator: str | None = None
    time_window: timedelta | None = None
    every_interval: timedelta | None = None

    @property
    def using_features(self) -> list[FeatureFactory]:
        return [self.feature]

    def compile(self) -> Transformation:
        from aligned.schemas.transformation import ConcatStringAggregation

        return ConcatStringAggregation(
            key=self.feature.feature_referance().name,
            separator=self.separator or '',
        )

    def aggregate_over(
        self, group_by: list[FeatureReferance], time_column: FeatureReferance | None
    ) -> AggregateOver:
        return aggregate_over(group_by, time_column, self.time_window, self.every_interval, None)


@dataclass
class SumAggregationFactory(TransformationFactory, AggregationTransformationFactory):

    feature: FeatureFactory
    time_window: timedelta | None = None
    every_interval: timedelta | None = None

    @property
    def using_features(self) -> list[FeatureFactory]:
        return [self.feature]

    def compile(self) -> Transformation:
        from aligned.schemas.transformation import SumAggregation

        return SumAggregation(
            key=self.feature.feature_referance().name,
        )

    def aggregate_over(
        self, group_by: list[FeatureReferance], time_column: FeatureReferance | None
    ) -> AggregateOver:
        return aggregate_over(group_by, time_column, self.time_window, self.every_interval, None)


@dataclass
class MeanAggregationFactory(TransformationFactory, AggregationTransformationFactory):

    feature: FeatureFactory
    time_window: timedelta | None = None
    every_interval: timedelta | None = None

    @property
    def using_features(self) -> list[FeatureFactory]:
        return [self.feature]

    def compile(self) -> Transformation:
        from aligned.schemas.transformation import MeanAggregation

        return MeanAggregation(
            key=self.feature.feature_referance().name,
        )

    def aggregate_over(
        self, group_by: list[FeatureReferance], time_column: FeatureReferance | None
    ) -> AggregateOver:
        return aggregate_over(group_by, time_column, self.time_window, self.every_interval, None)


@dataclass
class MinAggregationFactory(TransformationFactory, AggregationTransformationFactory):

    feature: FeatureFactory
    time_window: timedelta | None = None
    every_interval: timedelta | None = None

    @property
    def using_features(self) -> list[FeatureFactory]:
        return [self.feature]

    def compile(self) -> Transformation:
        from aligned.schemas.transformation import MinAggregation

        return MinAggregation(
            key=self.feature.feature_referance().name,
        )

    def aggregate_over(
        self, group_by: list[FeatureReferance], time_column: FeatureReferance | None
    ) -> AggregateOver:
        return aggregate_over(group_by, time_column, self.time_window, self.every_interval, None)


@dataclass
class MaxAggregationFactory(TransformationFactory, AggregationTransformationFactory):

    feature: FeatureFactory
    time_window: timedelta | None = None
    every_interval: timedelta | None = None

    @property
    def using_features(self) -> list[FeatureFactory]:
        return [self.feature]

    def compile(self) -> Transformation:
        from aligned.schemas.transformation import MaxAggregation

        return MaxAggregation(
            key=self.feature.feature_referance().name,
        )

    def aggregate_over(
        self, group_by: list[FeatureReferance], time_column: FeatureReferance | None
    ) -> AggregateOver:
        return aggregate_over(group_by, time_column, self.time_window, self.every_interval, None)


@dataclass
class CountAggregationFactory(TransformationFactory, AggregationTransformationFactory):

    feature: FeatureFactory
    time_window: timedelta | None = None
    every_interval: timedelta | None = None

    @property
    def using_features(self) -> list[FeatureFactory]:
        return [self.feature]

    def compile(self) -> Transformation:
        from aligned.schemas.transformation import CountAggregation

        return CountAggregation(
            key=self.feature.feature_referance().name,
        )

    def aggregate_over(
        self, group_by: list[FeatureReferance], time_column: FeatureReferance | None
    ) -> AggregateOver:
        return aggregate_over(group_by, time_column, self.time_window, self.every_interval, None)


@dataclass
class CountDistinctAggregationFactory(TransformationFactory, AggregationTransformationFactory):

    feature: FeatureFactory
    time_window: timedelta | None = None
    every_interval: timedelta | None = None

    @property
    def using_features(self) -> list[FeatureFactory]:
        return [self.feature]

    def compile(self) -> Transformation:
        from aligned.schemas.transformation import CountDistinctAggregation

        return CountDistinctAggregation(
            key=self.feature.feature_referance().name,
        )

    def aggregate_over(
        self, group_by: list[FeatureReferance], time_column: FeatureReferance | None
    ) -> AggregateOver:
        return aggregate_over(group_by, time_column, self.time_window, self.every_interval, None)


@dataclass
class StdAggregationFactory(TransformationFactory, AggregationTransformationFactory):

    feature: FeatureFactory
    time_window: timedelta | None = None
    every_interval: timedelta | None = None

    @property
    def using_features(self) -> list[FeatureFactory]:
        return [self.feature]

    def compile(self) -> Transformation:
        from aligned.schemas.transformation import StdAggregation

        return StdAggregation(
            key=self.feature.feature_referance().name,
        )

    def aggregate_over(
        self, group_by: list[FeatureReferance], time_column: FeatureReferance | None
    ) -> AggregateOver:
        return aggregate_over(group_by, time_column, self.time_window, self.every_interval, None)


@dataclass
class VarianceAggregationFactory(TransformationFactory, AggregationTransformationFactory):

    feature: FeatureFactory
    time_window: timedelta | None = None
    every_interval: timedelta | None = None

    @property
    def using_features(self) -> list[FeatureFactory]:
        return [self.feature]

    def compile(self) -> Transformation:
        from aligned.schemas.transformation import VarianceAggregation

        return VarianceAggregation(
            key=self.feature.feature_referance().name,
        )

    def aggregate_over(
        self, group_by: list[FeatureReferance], time_column: FeatureReferance | None
    ) -> AggregateOver:
        return aggregate_over(group_by, time_column, self.time_window, self.every_interval, None)


@dataclass
class MedianAggregationFactory(TransformationFactory, AggregationTransformationFactory):

    feature: FeatureFactory
    time_window: timedelta | None = None
    every_interval: timedelta | None = None

    @property
    def using_features(self) -> list[FeatureFactory]:
        return [self.feature]

    def compile(self) -> Transformation:
        from aligned.schemas.transformation import MedianAggregation

        return MedianAggregation(
            key=self.feature.feature_referance().name,
        )

    def aggregate_over(
        self, group_by: list[FeatureReferance], time_column: FeatureReferance | None
    ) -> AggregateOver:
        return aggregate_over(group_by, time_column, self.time_window, self.every_interval, None)


@dataclass
class PercentileAggregationFactory(TransformationFactory, AggregationTransformationFactory):

    feature: FeatureFactory
    percentile: float
    time_window: timedelta | None = None
    every_interval: timedelta | None = None

    @property
    def using_features(self) -> list[FeatureFactory]:
        return [self.feature]

    def compile(self) -> Transformation:
        from aligned.schemas.transformation import PercentileAggregation

        return PercentileAggregation(
            key=self.feature.feature_referance().name,
            percentile=self.percentile,
        )

    def aggregate_over(
        self, group_by: list[FeatureReferance], time_column: FeatureReferance | None
    ) -> AggregateOver:
        return aggregate_over(group_by, time_column, self.time_window, self.every_interval, None)
