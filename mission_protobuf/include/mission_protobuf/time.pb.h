// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: time.proto

#ifndef PROTOBUF_time_2eproto__INCLUDED
#define PROTOBUF_time_2eproto__INCLUDED

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 2006000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 2006001 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)

namespace mission_protobuf {

// Internal implementation detail -- do not call these.
void  protobuf_AddDesc_time_2eproto();
void protobuf_AssignDesc_time_2eproto();
void protobuf_ShutdownFile_time_2eproto();

class Time;

// ===================================================================

class Time : public ::google::protobuf::Message {
 public:
  Time();
  virtual ~Time();

  Time(const Time& from);

  inline Time& operator=(const Time& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _unknown_fields_;
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return &_unknown_fields_;
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const Time& default_instance();

  void Swap(Time* other);

  // implements Message ----------------------------------------------

  Time* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const Time& from);
  void MergeFrom(const Time& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const;
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  public:
  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // required int64 sec = 1;
  inline bool has_sec() const;
  inline void clear_sec();
  static const int kSecFieldNumber = 1;
  inline ::google::protobuf::int64 sec() const;
  inline void set_sec(::google::protobuf::int64 value);

  // required int64 nsec = 2;
  inline bool has_nsec() const;
  inline void clear_nsec();
  static const int kNsecFieldNumber = 2;
  inline ::google::protobuf::int64 nsec() const;
  inline void set_nsec(::google::protobuf::int64 value);

  // @@protoc_insertion_point(class_scope:mission_protobuf.Time)
 private:
  inline void set_has_sec();
  inline void clear_has_sec();
  inline void set_has_nsec();
  inline void clear_has_nsec();

  ::google::protobuf::UnknownFieldSet _unknown_fields_;

  ::google::protobuf::uint32 _has_bits_[1];
  mutable int _cached_size_;
  ::google::protobuf::int64 sec_;
  ::google::protobuf::int64 nsec_;
  friend void  protobuf_AddDesc_time_2eproto();
  friend void protobuf_AssignDesc_time_2eproto();
  friend void protobuf_ShutdownFile_time_2eproto();

  void InitAsDefaultInstance();
  static Time* default_instance_;
};
// ===================================================================


// ===================================================================

// Time

// required int64 sec = 1;
inline bool Time::has_sec() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void Time::set_has_sec() {
  _has_bits_[0] |= 0x00000001u;
}
inline void Time::clear_has_sec() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void Time::clear_sec() {
  sec_ = GOOGLE_LONGLONG(0);
  clear_has_sec();
}
inline ::google::protobuf::int64 Time::sec() const {
  // @@protoc_insertion_point(field_get:mission_protobuf.Time.sec)
  return sec_;
}
inline void Time::set_sec(::google::protobuf::int64 value) {
  set_has_sec();
  sec_ = value;
  // @@protoc_insertion_point(field_set:mission_protobuf.Time.sec)
}

// required int64 nsec = 2;
inline bool Time::has_nsec() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void Time::set_has_nsec() {
  _has_bits_[0] |= 0x00000002u;
}
inline void Time::clear_has_nsec() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void Time::clear_nsec() {
  nsec_ = GOOGLE_LONGLONG(0);
  clear_has_nsec();
}
inline ::google::protobuf::int64 Time::nsec() const {
  // @@protoc_insertion_point(field_get:mission_protobuf.Time.nsec)
  return nsec_;
}
inline void Time::set_nsec(::google::protobuf::int64 value) {
  set_has_nsec();
  nsec_ = value;
  // @@protoc_insertion_point(field_set:mission_protobuf.Time.nsec)
}


// @@protoc_insertion_point(namespace_scope)

}  // namespace mission_protobuf

#ifndef SWIG
namespace google {
namespace protobuf {


}  // namespace google
}  // namespace protobuf
#endif  // SWIG

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_time_2eproto__INCLUDED
